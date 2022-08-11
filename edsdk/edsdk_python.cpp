#include "edsdk_python.h"
#include "datetime.h"

#include "EDSDK.h"
#include "edsdk_error_map.h"

#include <cassert>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>


#define PyCheck_EDSERROR(err) \
    if (err != EDS_ERR_OK) { \
    	PyObject *exc_args = PyTuple_New(2); \
	    PyTuple_SetItem(exc_args, 0, PyUnicode_FromString(EDS::errorMessage(err))); \
	    PyTuple_SetItem(exc_args, 1, PyLong_FromLong(err)); \
	    PyErr_SetObject(PyEdsError, exc_args); \
        return nullptr; \
    }


typedef struct {
    PyObject_HEAD
    EdsBaseRef edsObj;
} PyEdsObject;


static void PyEdsObject_dealloc(PyEdsObject* self)
{
	EdsRelease(self->edsObj);
	Py_TYPE(self)->tp_free((PyObject*) self);
}


static PyTypeObject PyEdsObjectType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "edsdk.api.EdsObject",        /* tp_name */
    sizeof(PyEdsObject),            /* tp_basicsize */
    0,                              /* tp_itemsize */
    (destructor)PyEdsObject_dealloc,/* tp_dealloc */
    0,                              /* tp_print */
    0,                              /* tp_getattr */
    0,                              /* tp_setattr */
    0,                              /* tp_reserved */
    0,                              /* tp_repr */
    0,                              /* tp_as_number */
    0,                              /* tp_as_sequence */
    0,                              /* tp_as_mapping */
    0,                              /* tp_hash  */
    0,                              /* tp_call */
    0,                              /* tp_str */
    0,                              /* tp_getattro */
    0,                              /* tp_setattro */
    0,                              /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,             /* tp_flags */
    PyDoc_STR("EdsObject object"),/* tp_doc */
};


static PyObject *PyEdsError;


static PyObject *PyEdsError_tp_str(PyObject *self)
{
	if (!PyObject_HasAttrString(self, "args")) {
		// This should never happen
		return PyUnicode_FromString("");
	}

	PyObject *ret = NULL;
	PyObject *args = PyObject_GetAttrString(self, "args");
	if (PyTuple_Size(args) < 1) {
		ret = PyObject_Repr(args);
	}
    else {
		PyObject *str = PyTuple_GetItem(args, 0);
		ret = PyObject_Str(str);
	}
	Py_XDECREF(args);
	return ret;
}



static PyObject *PyEdsError_getcode(PyObject *self, void *closure)
{
	// Like before, but with less checks, it is okay for this function to fail
	PyObject *args = PyObject_GetAttrString(self, "args");
	if (!args) {
		return NULL;
	}

	PyObject *ret = PyTuple_GetItem(args, 1);
	Py_XINCREF(ret);
	Py_XDECREF(args);
	return ret;
}


static PyGetSetDef PyEdsError_getsetters[] = {
	{"code", PyEdsError_getcode, NULL, NULL, NULL},
	{NULL}
};


bool PyCallable_CheckNumberOfParameters(PyObject* callable, const long n){
    bool result = false;
    if(PyObject* pyCode = PyObject_GetAttrString(callable, "__code__")) {
        if(PyObject* pyArgCount = PyObject_GetAttrString(pyCode, "co_argcount")) {
            const long argcount = PyLong_AsLong(pyArgCount);
            if (argcount == n) {
                result = true;
            }
            // check if the function accepts *args
            else if (PyObject* pyFlags = PyObject_GetAttrString(pyCode, "co_flags"))
            {
                const long flags = PyLong_AsLong(pyFlags);
                // bit CO_VARARGS is set if the function uses the *arguments syntax
                // to accept an arbitrary number of positional arguments
                if (argcount < n && flags & CO_VARARGS) {
                    result = true;
                }
                Py_DECREF(pyFlags);
            }
            Py_DECREF(pyArgCount);
        }
        Py_DECREF(pyCode);
    }
    return result;
}


inline PyObject* PyEdsObject_New(EdsBaseRef inObject) {
    if (!inObject) {
        PyErr_Format(PyExc_TypeError, "EdsBaseRef expected %p", inObject);
    }
    PyEdsObject* pyObj = (PyEdsObject*)PyObject_New(PyEdsObject, &PyEdsObjectType);
    if (!pyObj) {
        PyErr_Format(PyExc_MemoryError, "failed to create EdsObject");
        return nullptr;
    }
    pyObj->edsObj = inObject;
    return (PyObject*)pyObj;
}


inline PyEdsObject* PyToEds(PyObject* inObject) {
    if (!PyObject_TypeCheck(inObject, &PyEdsObjectType)) {
        PyErr_Format(PyExc_ValueError, "invalid EdsObject %p", inObject);
        return nullptr;
    }
    return reinterpret_cast<PyEdsObject*>(inObject);
}


template<typename T>
inline PyObject* GetEnum(const char* moduleName, const char* enumClassName, const T enumValue){
    PyObject* module = PyImport_AddModule(moduleName);
    if (!module) {
        std::cout << "failed to import module " << moduleName << std::endl;
        PyErr_Format(PyExc_ValueError, "failed to import module %s", moduleName);
        return nullptr;
    }
    PyObject* enumClass = PyObject_GetAttrString(module, enumClassName);
    if (!enumClass) {
        std::cout << "failed to get enum class " << enumClassName << std::endl;
        PyErr_Format(PyExc_ValueError, "failed to get enum class %s", enumClassName);
        return nullptr;
    }
    PyObject* enumValueObj = PyObject_CallFunction(enumClass, "(i)", enumValue);
    if (!enumValueObj) {
        std::cout << "failed to call enum class " << enumClassName << std::endl;
        PyErr_Format(PyExc_ValueError, "failed to get enum value %s", enumValue);
        Py_DECREF(enumClass);
        return nullptr;
    }

    Py_DECREF(enumClass);
    return enumValueObj;
}


static std::map<EdsDataType const, std::size_t const> const EdsDataTypeSize = {
    {kEdsDataType_Bool, sizeof(EdsBool)},
    {kEdsDataType_Int8, sizeof(EdsInt8)},
    {kEdsDataType_UInt8, sizeof(EdsUInt8)},
    {kEdsDataType_Int16, sizeof(EdsInt16)},
    {kEdsDataType_UInt16, sizeof(EdsUInt16)},
    {kEdsDataType_Int32, sizeof(EdsInt32)},
    {kEdsDataType_UInt32, sizeof(EdsUInt32)},
    {kEdsDataType_Int64, sizeof(EdsInt64)},
    {kEdsDataType_UInt64, sizeof(EdsUInt64)},
    {kEdsDataType_Float, sizeof(EdsFloat)},
    {kEdsDataType_Double, sizeof(EdsDouble)},
    {kEdsDataType_Rational, sizeof(EdsRational)},
    {kEdsDataType_Point, sizeof(EdsPoint)},
    {kEdsDataType_Rect, sizeof(EdsRect)},
    {kEdsDataType_Time, sizeof(EdsTime)},
    {kEdsDataType_FocusInfo, sizeof(EdsFocusInfo)},
    {kEdsDataType_PictureStyleDesc, sizeof(EdsPictureStyleDesc)},
};


PyDoc_STRVAR(PyEds_InitializeSDK__doc__,
"Initializes the libraries.\n"
"When using the EDSDK libraries, you must call this API once\n"
"\tbefore using EDSDK APIs.\n\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_InitializeSDK(PyObject *Py_UNUSED(self)) {
    unsigned long retVal(EdsInitializeSDK());
    PyCheck_EDSERROR(retVal);
    return PyLong_FromUnsignedLong(retVal);
}


PyDoc_STRVAR(PyEds_TerminateSDK__doc__,
"Terminates use of the libraries.\n"
"This function muse be called when ending the SDK.\n"
"Calling this function releases all resources allocated by the libraries.\n\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_TerminateSDK(PyObject *Py_UNUSED(self)) {
    unsigned long retVal(EdsTerminateSDK());
    PyCheck_EDSERROR(retVal);
    return PyLong_FromUnsignedLong(retVal);
}


PyDoc_STRVAR(PyEds_GetCameraList__doc__,
"Gets camera list objects.\n\n"
":raises EdsError: Any of the sdk errors.\n"
":return EdsObject: the camera-list.");

static PyObject* PyEds_GetCameraList(PyObject *Py_UNUSED(self)) {
    EdsCameraListRef cameraList;
    unsigned long retVal(EdsGetCameraList(&cameraList));
    PyCheck_EDSERROR(retVal);
    return PyEdsObject_New(cameraList);
}


PyDoc_STRVAR(PyEds_GetChildCount__doc__,
"Gets the number of child objects of the designated object.\n"
"Example: Number of files in a directory\n\n"
":param EdsObject parent: the list object.\n"
":raises EdsError: Any of the sdk errors.\n"
":return int: Number of elements in this list.");

static PyObject* PyEds_GetChildCount(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    if (!PyArg_ParseTuple(args, "O:EdsGetChildCount", &pyObj)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }
    unsigned long childCount;
    unsigned long retVal(EdsGetChildCount(edsObj->edsObj, &childCount));
    PyCheck_EDSERROR(retVal);
    return PyLong_FromUnsignedLong(childCount);
}


PyDoc_STRVAR(PyEds_GetChildAtIndex__doc__,
"Gets an indexed child object of the designated object\n\n"
":param EdsObject parent: the list object.\n"
":param int index: The index that is passed in, is zero based.\n"
":raises EdsError: Any of the sdk errors.\n"
":return EdsObject: the child object.");

static PyObject* PyEds_GetChildAtIndex(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    long index;
    if (!PyArg_ParseTuple(args, "Ol:EdsGetChildAtIndex", &pyObj, &index)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }
    EdsBaseRef child;
    unsigned long retVal(EdsGetChildAtIndex(edsObj->edsObj, index, &child));
    PyCheck_EDSERROR(retVal);
    return PyEdsObject_New(child);
}


PyDoc_STRVAR(PyEds_OpenSession__doc__,
"Establishes a logical connection with a remote camera.\n"
"Use this API after getting the camera's EdsCamera object.\n\n"
":param PyEdsObject camera: the camera.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_OpenSession(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    if (!PyArg_ParseTuple(args, "O:EdsOpenSession", &pyObj)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }
    unsigned long retVal(EdsOpenSession(edsObj->edsObj));
    PyCheck_EDSERROR(retVal);
    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_CloseSession__doc__,
"Closes a logical connection with a remote camera.\n\n"
":param PyEdsObject camera: the camera.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_CloseSession(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    if (!PyArg_ParseTuple(args, "O:EdsCloseSession", &pyObj)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }
    unsigned long retVal(EdsCloseSession(edsObj->edsObj));
    PyCheck_EDSERROR(retVal);
    Py_RETURN_NONE;
}


PyObject* pySetCameraStateCallback = nullptr;

PyDoc_STRVAR(PyEds_SetCameraStateEventHandler__doc__,
"Registers a callback function for receiving status\n"
"\tchange notification events for property states on a camera\n\n"
":param PyEdsObject camera: the camera object.\n"
":param StateEvent event: the event to be supplemented.\n"
"\tTo designate all events, use StateEvent.All.\n"
":param Callable callback: the callback for receiving the events.\n"
"\tExpected signature (event: StateEvent, event_data: int) -> int.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetCameraStateEventHandler(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    unsigned long event;
    PyObject* pyCallable;
    // PyObject* pyContext;
    if (!PyArg_ParseTuple(args, "OkO:EdsSetCameraStateEventHandler", &pyObj, &event, &pyCallable)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }

    if (pyCallable == Py_None || !PyCallable_Check(pyCallable)){

        PyErr_Format(PyExc_ValueError, "expected a callable object");
        return nullptr;
    }

    if (!PyCallable_CheckNumberOfParameters(pyCallable, 2)) {
        PyErr_Format(PyExc_ValueError, "expected a callable object with 2 parameters (inEvent, inEventData)");
        return nullptr;
    }

    if (pySetCameraStateCallback != nullptr) {
        Py_DECREF(pySetCameraStateCallback);
    }

    pySetCameraStateCallback = pyCallable;

    Py_INCREF(pySetCameraStateCallback);

    auto callbackWrapper = [](EdsStateEvent inEvent, EdsUInt32 inEventData, EdsVoid* inContext) -> EdsError {
        PyGILState_STATE gstate;
        gstate = PyGILState_Ensure();

        PyObject* pyEvent = GetEnum("edsdk.constants", "StateEvent", inEvent);
        if (pyEvent == nullptr) {
            PyErr_Clear();
            std::cout << "Unknown State Event: " << inEvent << std::endl;
            pyEvent = PyLong_FromUnsignedLong(inEvent);
        }
        PyObject* pyEventData = PyLong_FromUnsignedLong(inEventData);
        PyObject* pyContext = static_cast<PyObject *>(inContext);
        PyObject* pyRetVal = PyObject_CallFunctionObjArgs(pyContext, pyEvent, pyEventData, nullptr);
        if (pyRetVal == nullptr) {
            PyErr_Format(PyExc_ValueError, "unable to call the callback");
            Py_DECREF(pyEvent);
            Py_DECREF(pyEventData);
            return EDS_ERR_INVALID_FN_POINTER;
        }

        unsigned long retVal(PyLong_AsUnsignedLong(pyRetVal));
        Py_DECREF(pyEvent);
        Py_DECREF(pyEventData);
        Py_DECREF(pyRetVal);

        PyGILState_Release(gstate);
        return retVal;
    };

    unsigned long retVal(
        EdsSetCameraStateEventHandler(
            edsObj->edsObj, event,
            callbackWrapper,
            pySetCameraStateCallback));

    if (retVal != EDS_ERR_OK) {
        Py_DECREF(pySetCameraStateCallback);
        PyCheck_EDSERROR(retVal);
    }
    Py_RETURN_NONE;
}


static PyObject *pySetObjectCallback = nullptr;

PyDoc_STRVAR(PyEds_SetObjectEventHandler__doc__,
"Registers a callback function for receiving status\n"
"\tchange notification events for objects on a remote camera\n"
"Here, object means volumes representing memory cards, files and directories,\n"
"\tand shot images stored in memory, in particular.\n\n"
":param PyEdsObject camera: the camera object.\n"
":param ObjectEvent event: the event to be supplemented.\n"
"\tTo designate all events, use ObjectEvent.All.\n"
":param Callable callback: the callback for receiving events.\n"
"\tExpected signature (event: ObjectEvent, obj_ref: PyEdsObject) -> int.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetObjectEventHandler(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    unsigned long event;
    PyObject* pyCallable;
    if (!PyArg_ParseTuple(args, "OkO:EdsSetObjectEventHandler", &pyObj, &event, &pyCallable)) {
        return nullptr;
    }

    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }

    if (pyCallable == Py_None || !PyCallable_Check(pyCallable)){
        PyErr_Format(PyExc_ValueError, "expected a callable object");
        return nullptr;
    }

    if (!PyCallable_CheckNumberOfParameters(pyCallable, 2)) {
        PyErr_Format(PyExc_ValueError, "expected a callable object with 2 parameters (inEvent, inRef)");
        return nullptr;
    }

    if (pySetObjectCallback != nullptr) {
        Py_DECREF(pySetObjectCallback);
    }
    pySetObjectCallback = pyCallable;
    Py_INCREF(pySetObjectCallback);

    auto callbackWrapper = [](EdsStateEvent inEvent, EdsBaseRef inRef, EdsVoid* inContext) -> EdsError {

        PyGILState_STATE gstate;
        gstate = PyGILState_Ensure();

        PyObject* pyContext = static_cast<PyObject *>(inContext);
        PyObject* pyEvent = GetEnum("edsdk.constants", "ObjectEvent", inEvent);
        if (pyEvent == nullptr) {
            PyErr_Clear();
            std::cout << "Unknown Object Event: " << inEvent  << std::endl;
            pyEvent = PyLong_FromUnsignedLong(inEvent);
        }
        PyObject* pyInRef = PyEdsObject_New(inRef);
        PyObject* pyRetVal = PyObject_CallFunctionObjArgs(pyContext, pyEvent, pyInRef, nullptr);
        if (pyRetVal == nullptr) {
            PyErr_Format(PyExc_ValueError, "unable to call the callback");
            Py_DECREF(pyEvent);
            Py_DECREF(pyInRef);
            return EDS_ERR_INVALID_FN_POINTER;
        }
        unsigned long retVal(PyLong_AsUnsignedLong(pyRetVal));
        Py_DECREF(pyEvent);
        Py_DECREF(pyInRef);
        Py_DECREF(pyRetVal);

        PyGILState_Release(gstate);
        return retVal;
    };

    unsigned long retVal(EdsSetObjectEventHandler(edsObj->edsObj, event, callbackWrapper, pySetObjectCallback));

    if (retVal != EDS_ERR_OK) {
        Py_DECREF(pySetObjectCallback);
        PyCheck_EDSERROR(retVal);
    }
    Py_RETURN_NONE;
}


static PyObject *pySetPropertyCallback = nullptr;

PyDoc_STRVAR(PyEds_SetPropertyEventHandler__doc__,
"Registers a callback function for receiving status\n"
"\tchange notification events for property states on a camera.\n\n"
":param PyEdsObject camera: the camera object.\n"
":param PropertyEvent event: the event to be supplemented.\n"
"\tTo designate all events, use PropertyEvent.All.\n"
":param Callable callback: the callback for receiving events.\n"
"\tExpected signature (event: StateEvent, prop_id: PropID, param: int) -> int.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetPropertyEventHandler(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    unsigned long event;
    PyObject* pyCallable;

    if (!PyArg_ParseTuple(args, "OkO:EdsSetPropertyEventHandler", &pyObj, &event, &pyCallable)) {
        return nullptr;
    }

    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }

    if (pyCallable == Py_None || !PyCallable_Check(pyCallable)){
        PyErr_Format(PyExc_ValueError, "expected a callable object");
        return nullptr;
    }

    if (!PyCallable_CheckNumberOfParameters(pyCallable, 3)) {
        PyErr_Format(PyExc_ValueError, "expected a callable object with 3 parameters (inEvent, inPropertyID, inParam)");
        return nullptr;
    }

    if (pySetPropertyCallback != nullptr) {
        Py_DECREF(pySetPropertyCallback);
    }

    pySetPropertyCallback = pyCallable;

    Py_INCREF(pySetPropertyCallback);

    auto callbackWrapper = [](EdsPropertyEvent inEvent, EdsPropertyID inPropertyID, EdsUInt32 inParam, EdsVoid* inContext) -> EdsError {

        PyGILState_STATE gstate;
        gstate = PyGILState_Ensure();

        PyObject* pyContext = static_cast<PyObject *>(inContext);
        PyObject* pyEvent = GetEnum("edsdk.constants", "PropertyEvent", inEvent);
        if (pyEvent == nullptr) {
            PyErr_Clear();
            std::cout << "Unknown Property Event: " << inEvent  << std::endl;
            pyEvent = PyLong_FromUnsignedLong(inEvent);
        }
        PyObject* pyPropertyID = GetEnum("edsdk.constants", "PropID", inPropertyID);
        if (pyPropertyID == nullptr) {
            PyErr_Clear();
            std::cout << "Unknown Property ID: " << inPropertyID  << std::endl;
            pyPropertyID = PyLong_FromUnsignedLong(inPropertyID);
        }
        PyObject* pyParam = PyLong_FromUnsignedLong(inParam);

        PyObject* pyRetVal = PyObject_CallFunctionObjArgs(pyContext, pyEvent, pyPropertyID, pyParam, nullptr);
        if (pyRetVal == nullptr) {
            PyErr_Format(PyExc_ValueError, "unable to call the callback");
            Py_DECREF(pyEvent);
            Py_DECREF(pyPropertyID);
            Py_DECREF(pyParam);
            return EDS_ERR_INVALID_FN_POINTER;
        }
        unsigned long retVal(PyLong_AsUnsignedLong(pyRetVal));
        Py_DECREF(pyRetVal);
        Py_DECREF(pyEvent);
        Py_DECREF(pyParam);
        Py_DECREF(pyPropertyID);

        PyGILState_Release(gstate);
        return retVal;
    };

    unsigned long retVal(EdsSetPropertyEventHandler(edsObj->edsObj, event, callbackWrapper, pySetPropertyCallback));
    if (retVal != EDS_ERR_OK) {
        Py_DECREF(pySetPropertyCallback);
        PyCheck_EDSERROR(retVal);
    }
    Py_RETURN_NONE;

}


static PyObject *pyCameraAddedCallback = nullptr;

PyDoc_STRVAR(PyEds_SetCameraAddedHandler__doc__,
"Registers a callback function for when a camera is detected.\n\n"
":param Callable callback: the callback called when a camera is connected.\n"
"\tExpected signature () -> int.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetCameraAddedHandler(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyCallable;
    if (!PyArg_ParseTuple(args, "O:EdsSetCameraAddedHandler", &pyCallable)) {
        return nullptr;
    }

    if (pyCallable == Py_None || !PyCallable_Check(pyCallable)){
        PyErr_Format(PyExc_ValueError, "expected a callable object");
        return nullptr;
    }

    if (!PyCallable_CheckNumberOfParameters(pyCallable, 0)) {
        PyErr_Format(PyExc_ValueError, "expected a callable object with 0 parameters");
        return nullptr;
    }

    if (pyCameraAddedCallback != nullptr) {
        Py_DECREF(pyCameraAddedCallback);
    }
    pyCameraAddedCallback = pyCallable;

    Py_INCREF(pyCameraAddedCallback);

    auto callbackWrapper = [](EdsVoid* inContext) -> EdsError {
        PyGILState_STATE gstate;
        gstate = PyGILState_Ensure();

        PyObject* pyContext = static_cast<PyObject *>(inContext);
        PyObject* pyRetVal = PyObject_CallFunctionObjArgs(pyContext, nullptr);
        if (pyRetVal == nullptr) {
            PyErr_Format(PyExc_ValueError, "unable to call the callback");
            return EDS_ERR_INVALID_FN_POINTER;
        }
        unsigned long retVal(PyLong_AsUnsignedLong(pyRetVal));
        Py_DECREF(pyRetVal);

        PyGILState_Release(gstate);
        return retVal;
    };

    unsigned long retVal(
        EdsSetCameraAddedHandler(
            callbackWrapper,
            pyCameraAddedCallback));

    if (retVal != EDS_ERR_OK) {
        Py_DECREF(pyCameraAddedCallback);
        PyCheck_EDSERROR(retVal);
    }
    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_GetPropertySize__doc__,
"Gets the byte size and data type of a designated property\n"
"\tfrom a camera object or image object.\n\n"
":param PyEdsObject camera_or_image: the item object.\n"
":param PropID property_id: The property ID.\n"
":param int param: Specify an index in case there are two or\n"
"\tmore values over the same ID, defaults to 0.\n"
":raises EdsError: Any of the sdk errors.\n"
":return Tuple[DataType, int]: the property DataType and size in bytes.");

static PyObject* PyEds_GetPropertySize(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    unsigned long propertyID;
    long param = 0;
    if (!PyArg_ParseTuple(args, "Okl:EdsGetPropertySize", &pyObj, &propertyID, &param)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }
    EdsDataType dataType;
    unsigned long dataSize;

    unsigned long retVal(EdsGetPropertySize(edsObj->edsObj, propertyID, param, &dataType, &dataSize));
    PyCheck_EDSERROR(retVal);

    PyObject *pyEnumVal = GetEnum("edsdk.constants", "DataType", dataType);
    if (pyEnumVal == nullptr) {
        PyErr_Clear();
        std::cout << "Unknown Data Type: " << dataType  << std::endl;
        pyEnumVal = PyLong_FromUnsignedLong(dataType);
    }
    PyObject *result = PyTuple_New(2);
    PyTuple_SetItem(result, 0, pyEnumVal);
    PyTuple_SetItem(result, 1, PyLong_FromUnsignedLong(dataSize));

    return result;
}


PyDoc_STRVAR(PyEds_GetPropertyData__doc__,
"Gets property information from the designated object.\n\n"
":param PyEdsObject camera_or_image: The reference of the item.\n"
":param PropID property_id: The PropertyID.\n"
":param int param: Specify an index in case there are two or\n"
"\tmore values over the same ID, defaults to 0.\n"
":raises EdsError: Any of the sdk errors.\n"
":return Any: The property value.");

static PyObject* PyEds_GetPropertyData(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject* pyObj;
    unsigned long propertyID;
    long param = 0;
    if (!PyArg_ParseTuple(args, "Okl:EdsGetPropertyData", &pyObj, &propertyID, &param)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }

    EdsDataType dataType;
    unsigned long dataSize;

    unsigned long retVal(EdsGetPropertySize(edsObj->edsObj, propertyID, param, &dataType, &dataSize));
    PyCheck_EDSERROR(retVal);

    PyObject *pyPropertyData = nullptr;
    void *propertyData = new (std::nothrow) uint8_t[dataSize];
    if (propertyData == nullptr) {
        PyErr_NoMemory();
        return nullptr;
    }
    retVal = EdsGetPropertyData(edsObj->edsObj, propertyID, param, dataSize, propertyData);
    PyCheck_EDSERROR(retVal);
    switch (dataType){
        case kEdsDataType_Bool: {
            pyPropertyData = PyBool_FromLong(*static_cast<int *>(propertyData));
            break;
        }
        case kEdsDataType_String: {
            pyPropertyData = PyUnicode_DecodeFSDefault(static_cast<char *>(propertyData));
            break;
        }
        case kEdsDataType_UInt8:
        case kEdsDataType_UInt16:
        case kEdsDataType_UInt32: {
            if (propertyID == kEdsPropID_BatteryQuality) {
                pyPropertyData = GetEnum("edsdk.constants", "BatteryQuality", *static_cast<int *>(propertyData));
                if (pyPropertyData == nullptr) {
                    PyErr_Clear();
                    std::cout << "Unknown Battery Quality: " << *static_cast<int *>(propertyData) << std::endl;
                    pyPropertyData = PyLong_FromUnsignedLong(*static_cast<unsigned long *>(propertyData));
                }
                break;
            }
            pyPropertyData = PyLong_FromUnsignedLong(*static_cast<unsigned long*>(propertyData));
            break;
        }
        case kEdsDataType_UInt64: {
            pyPropertyData = PyLong_FromUnsignedLongLong(*static_cast<unsigned long long *>(propertyData));
            break;
        }
        case kEdsDataType_Int8:
        case kEdsDataType_Int16:
        case kEdsDataType_Int32: {
            pyPropertyData = PyLong_FromLong(*static_cast<long*>(propertyData));
            break;
        }
        case kEdsDataType_Int64: {
            pyPropertyData = PyLong_FromLongLong(*static_cast<long long*>(propertyData));
            break;
        }
        case kEdsDataType_Float:
        case kEdsDataType_Double: {
            pyPropertyData = PyFloat_FromDouble(*static_cast<double*>(propertyData));
            break;
        }
        case kEdsDataType_Rational: {
            EdsRational *rational = static_cast<EdsRational *>(propertyData);
            pyPropertyData = PyTuple_New(2);
            PyTuple_SetItem(pyPropertyData, 0, PyLong_FromLong(rational->numerator));
            PyTuple_SetItem(pyPropertyData, 1, PyLong_FromUnsignedLong(rational->denominator));
            break;
        }
        case kEdsDataType_Point: {
            EdsPoint *point = static_cast<EdsPoint *>(propertyData);
            pyPropertyData = PyTuple_New(2);
            PyTuple_SetItem(pyPropertyData, 0, PyLong_FromLong(point->x));
            PyTuple_SetItem(pyPropertyData, 1, PyLong_FromLong(point->y));
            break;
        }
        case kEdsDataType_Rect: {
            EdsRect *rect = static_cast<EdsRect *>(propertyData);
            pyPropertyData = PyTuple_New(4);
            PyTuple_SetItem(pyPropertyData, 0, PyLong_FromLong(rect->point.x));
            PyTuple_SetItem(pyPropertyData, 1, PyLong_FromLong(rect->point.y));
            PyTuple_SetItem(pyPropertyData, 2, PyLong_FromLong(rect->size.width));
            PyTuple_SetItem(pyPropertyData, 3, PyLong_FromLong(rect->size.height));
            break;
        }
        case kEdsDataType_Time: {
            EdsTime *t = static_cast<EdsTime *>(propertyData);
            PyDateTime_IMPORT;
            pyPropertyData = PyDateTime_FromDateAndTime(
                static_cast<int>(t->year),
                static_cast<int>(t->month),
                static_cast<int>(t->day),
                static_cast<int>(t->hour),
                static_cast<int>(t->minute),
                static_cast<int>(t->second),
                static_cast<int>(t->milliseconds));
            break;
        }
        case kEdsDataType_ByteBlock: {
            pyPropertyData = PyBytes_FromStringAndSize(static_cast<char *>(propertyData), dataSize);
            break;
        }
        case kEdsDataType_FocusInfo:{
            EdsFocusInfo *focusInfo = static_cast<EdsFocusInfo *>(propertyData);
            pyPropertyData = PyDict_New();
            PyObject *pyImageRect = PyTuple_New(4);
            PyTuple_SetItem(pyImageRect, 0, PyLong_FromLong(focusInfo->imageRect.point.x));
            PyTuple_SetItem(pyImageRect, 1, PyLong_FromLong(focusInfo->imageRect.point.y));
            PyTuple_SetItem(pyImageRect, 2, PyLong_FromLong(focusInfo->imageRect.size.width));
            PyTuple_SetItem(pyImageRect, 3, PyLong_FromLong(focusInfo->imageRect.size.height));
            PyObject *pyFocusPointTuple = PyTuple_New(1053);
            for (int i = 0; i < 1053; i++) {
                PyObject *pyFocusPoint = PyDict_New();
                PyDict_SetItemString(pyFocusPoint, "valid", PyLong_FromUnsignedLong(focusInfo->focusPoint[i].valid));
                PyDict_SetItemString(pyFocusPoint, "selected", PyLong_FromUnsignedLong(focusInfo->focusPoint[i].selected));
                PyDict_SetItemString(pyFocusPoint, "justFocus", PyLong_FromUnsignedLong(focusInfo->focusPoint[i].justFocus));

                PyObject *pyRect = PyTuple_New(4);
                PyTuple_SetItem(pyRect, 0, PyLong_FromLong(focusInfo->focusPoint[i].rect.point.x));
                PyTuple_SetItem(pyRect, 1, PyLong_FromLong(focusInfo->focusPoint[i].rect.point.y));
                PyTuple_SetItem(pyRect, 2, PyLong_FromLong(focusInfo->focusPoint[i].rect.size.width));
                PyTuple_SetItem(pyRect, 3, PyLong_FromLong(focusInfo->focusPoint[i].rect.size.height));

                PyObject *pyReserved = PyLong_FromUnsignedLong(focusInfo->focusPoint[i].reserved);
                PyDict_SetItemString(pyFocusPoint, "rect", pyRect);
                PyDict_SetItemString(pyFocusPoint, "reserved", pyReserved);

                PyTuple_SetItem(pyFocusPointTuple, i, pyFocusPoint);

                Py_DECREF(pyRect);
                Py_DECREF(pyReserved);
            }
            PyObject *pyPointNumber = PyLong_FromUnsignedLong(focusInfo->pointNumber);
            PyObject *pyExecuteMode = PyLong_FromUnsignedLong(focusInfo->executeMode);

            PyDict_SetItemString(pyPropertyData, "imageRect", pyImageRect);
            PyDict_SetItemString(pyPropertyData, "pointNumber", pyPointNumber);
            PyDict_SetItemString(pyPropertyData, "focusPoint", pyFocusPointTuple);
            PyDict_SetItemString(pyPropertyData, "executeMode", pyExecuteMode);

            Py_DECREF(pyImageRect);
            Py_DECREF(pyPointNumber);
            Py_DECREF(pyFocusPointTuple);
            Py_DECREF(pyExecuteMode);
            break;
        }
        case kEdsDataType_PictureStyleDesc:{
            EdsPictureStyleDesc *pictureStyleDesc = static_cast<EdsPictureStyleDesc *>(propertyData);
            pyPropertyData = PyDict_New();
            PyObject *pyContrast = PyLong_FromLong(pictureStyleDesc->contrast);
            PyDict_SetItemString(pyPropertyData, "contrast", pyContrast);
            PyObject *pySharpness = PyLong_FromUnsignedLong(pictureStyleDesc->sharpness);
            PyDict_SetItemString(pyPropertyData, "sharpness", pySharpness);
            PyObject *pySaturation = PyLong_FromLong(pictureStyleDesc->saturation);
            PyDict_SetItemString(pyPropertyData, "saturation", pySaturation);
            PyObject *pyColorTone = PyLong_FromLong(pictureStyleDesc->colorTone);
            PyDict_SetItemString(pyPropertyData, "colorTone", pyColorTone);
            PyObject *pyFilterEffect = PyLong_FromUnsignedLong(pictureStyleDesc->filterEffect);
            PyDict_SetItemString(pyPropertyData, "filterEffect", pyFilterEffect);
            PyObject *pyToningEffect = PyLong_FromUnsignedLong(pictureStyleDesc->toningEffect);
            PyDict_SetItemString(pyPropertyData, "toningEffect", pyToningEffect);
            PyObject *pySharpFineness = PyLong_FromUnsignedLong(pictureStyleDesc->sharpFineness);
            PyDict_SetItemString(pyPropertyData, "sharpFineness", pySharpFineness);
            PyObject *pySharpThreshold = PyLong_FromUnsignedLong(pictureStyleDesc->sharpThreshold);
            PyDict_SetItemString(pyPropertyData, "sharpThreshold", pySharpThreshold);

            Py_DECREF(pyContrast);
            Py_DECREF(pySharpness);
            Py_DECREF(pySaturation);
            Py_DECREF(pyColorTone);
            Py_DECREF(pyFilterEffect);
            Py_DECREF(pyToningEffect);
            Py_DECREF(pySharpFineness);
            Py_DECREF(pySharpThreshold);
            break;
        }
        case kEdsDataType_Unknown:
        case kEdsDataType_Bool_Array:
        case kEdsDataType_Int8_Array:
        case kEdsDataType_Int16_Array:
        case kEdsDataType_Int32_Array:
        case kEdsDataType_UInt8_Array:
        case kEdsDataType_UInt16_Array:
        case kEdsDataType_UInt32_Array:
        case kEdsDataType_Rational_Array:{
            PyErr_Format(PyExc_NotImplementedError, "unable to get the property %ls", propertyID);
            delete propertyData;
            return nullptr;
        }
    }
    delete propertyData;
    return pyPropertyData;
}


PyDoc_STRVAR(PyEds_SetPropertyData__doc__,
"Sets property data for the designated object.\n\n"
":param PyEdsObject camera_or_image: The item object.\n"
":param PropID property_id: The PropertyID.\n"
":param int param: Specify an index in case there are two or\n"
"\tmore values over the same ID.\n",
":param Any data: The data to set.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetPropertyData(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject *pyObj;
    unsigned long propertyID;
    long param;
    PyObject *pyPropertyData;

    if (!PyArg_ParseTuple(args, "OklO:EdsSetPropertyData", &pyObj, &propertyID, &param, &pyPropertyData)) {
        return nullptr;
    }
    PyEdsObject* edsObj = PyToEds(pyObj);
    if (!edsObj) {
        return nullptr;
    }

    EdsDataType dataType;
    unsigned long dataSize;
    unsigned long retVal(EdsGetPropertySize(edsObj->edsObj, propertyID, param, &dataType, &dataSize));
    PyCheck_EDSERROR(retVal);

    uint8_t *propertyData = nullptr;
    if (EdsDataTypeSize.count(dataType)){
        propertyData = new (std::nothrow) uint8_t[EdsDataTypeSize.at(dataType)];
    }
    switch (dataType){
        case kEdsDataType_Bool: {
            if (!PyBool_Check(pyPropertyData))
            {
                PyErr_Format(PyExc_TypeError, "Properppty %lu expects boolean", propertyID);
                delete propertyData;
                return nullptr;
            }
            *propertyData = PyObject_IsTrue(pyPropertyData) ? true : false;
            break;
        }
        case kEdsDataType_String: {
            if (!PyUnicode_Check(pyPropertyData)) {
                PyErr_Format(PyExc_TypeError, "Property %lu expects string", propertyID);
                return nullptr;
            }
            PyObject* pyString = PyUnicode_AsEncodedString(pyPropertyData, Py_FileSystemDefaultEncoding, Py_FileSystemDefaultEncodeErrors);
            propertyData = reinterpret_cast<uint8_t *>(strdup(PyBytes_AsString(pyString)));
            if (!propertyData) {
                propertyData = nullptr;  // capture error later
            }
            Py_DecRef(pyString);
            break;
        }
    case kEdsDataType_UInt8:
    case kEdsDataType_UInt16:
    case kEdsDataType_UInt32: {
        if (!PyLong_Check(pyPropertyData)) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects unsigned int", propertyID);
            delete propertyData;
            return nullptr;
        }
        unsigned long uLongVal = PyLong_AsUnsignedLong(pyPropertyData);
        memcpy_s(propertyData, EdsDataTypeSize.at(dataType), &uLongVal, sizeof(unsigned long));
        break;
    }
    case kEdsDataType_UInt64: {
        if (!PyLong_Check(pyPropertyData)) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects unsigned int", propertyID);
            delete propertyData;
            return nullptr;
        }
        unsigned long long uLongLongVal = PyLong_AsUnsignedLongLong(pyPropertyData);
        memcpy_s(propertyData, EdsDataTypeSize.at(dataType), &uLongLongVal, sizeof(unsigned long long));
        break;
    }
    case kEdsDataType_Int8:
    case kEdsDataType_Int16:
    case kEdsDataType_Int32: {
        if (!PyLong_Check(pyPropertyData)) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects int", propertyID);
            delete propertyData;
            return nullptr;
        }
        long longVal = PyLong_AsLong(pyPropertyData);
        memcpy_s(propertyData, EdsDataTypeSize.at(dataType), &longVal, sizeof(long));
        break;
    }
    case kEdsDataType_Int64: {
        if (!PyLong_Check(pyPropertyData)) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects int", propertyID);
            delete propertyData;
            return nullptr;
        }
        long long longLongVal = PyLong_AsLongLong(pyPropertyData);
        memcpy_s(propertyData, EdsDataTypeSize.at(dataType), &longLongVal, sizeof(long long));
        break;
    }
    case kEdsDataType_Float:
    case kEdsDataType_Double: {
        if (!PyFloat_Check(pyPropertyData)) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects float", propertyID);
            delete propertyData;
            return nullptr;
        }
        double doubleVal = PyFloat_AsDouble(pyPropertyData);
        memcpy_s(propertyData, EdsDataTypeSize.at(dataType), &doubleVal, sizeof(double));
        break;
    }
    case kEdsDataType_Rational: {
        PyObject *iter = PyObject_GetIter(pyPropertyData);
        bool error = false;
        EdsRational *rational = reinterpret_cast<EdsRational *>(propertyData);
        if (iter) {
            PyObject *item = PyIter_Next(iter);
            if (!item || !PyLong_Check(item)) {
                error = true;
            }
            else {
                rational->numerator = PyLong_AsLong(item);
                Py_DECREF(item);
                item = PyIter_Next(iter);
                if (!item || !PyLong_Check(item)) {
                    error = true;
                }
                else {
                    rational->denominator = PyLong_AsUnsignedLong(item);
                    Py_DECREF(item);
                }
            }
            Py_DECREF(iter);
        } else {
            error = true;
        }
        if (error) {
            PyErr_Format(PyExc_TypeError, "Property %lu expects a sequence of two ints", propertyID);
            PyErr_Format(PyExc_TypeError, "Property %lu expects a sequence of two ints", propertyID);
            delete propertyData;
            return nullptr;
        }
        break;
    }
    case kEdsDataType_Unknown:
    case kEdsDataType_ByteBlock:
    case kEdsDataType_Point:
    case kEdsDataType_Rect:
    case kEdsDataType_Time:
    case kEdsDataType_FocusInfo:
    case kEdsDataType_PictureStyleDesc:
    case kEdsDataType_Bool_Array:
    case kEdsDataType_Int8_Array:
    case kEdsDataType_Int16_Array:
    case kEdsDataType_Int32_Array:
    case kEdsDataType_UInt8_Array:
    case kEdsDataType_UInt16_Array:
    case kEdsDataType_UInt32_Array:
    case kEdsDataType_Rational_Array:{
        PyErr_Format(PyExc_NotImplementedError, "unable to get the property %ls", propertyID);
        delete propertyData;
        return nullptr;
    }
    }
    if (propertyData == nullptr) {
        PyErr_Format(PyExc_MemoryError, "failed to allocate memory");
        return nullptr;
    }
    retVal = EdsSetPropertyData(edsObj->edsObj, propertyID, param, dataSize, propertyData);
    PyCheck_EDSERROR(retVal);

    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_GetDeviceInfo__doc__,
"Gets device information, such as the device name.\n"
"Because device information of remote cameras is stored\n"
"\ton the host computer, you can use this API\n"
"\tbefore the camera object initiates communication\n"
"\t(that is, before a session is opened).\n\n"
":param PyEdsObject camera: The camera object.\n"
":raises EdsError: Any of the sdk errors.\n"
":return Dict[str, Any]: The device information.");

static PyObject* PyEds_GetDeviceInfo(PyObject *Py_UNUSED(self), PyObject *cam){
    PyEdsObject *pyEdsCam = PyToEds(cam);
    if (!pyEdsCam) {
        return nullptr;
    }
    EdsDeviceInfo deviceInfo;
    unsigned long retVal(EdsGetDeviceInfo(pyEdsCam->edsObj, &deviceInfo));
    PyCheck_EDSERROR(retVal);

    PyObject* pyDeviceSubtype = GetEnum("edsdk.constants", "DeviceSubType", deviceInfo.deviceSubType);
    if (pyDeviceSubtype == nullptr) {
        PyErr_Clear();
        std::cout << "Unknown device subtype: " << deviceInfo.deviceSubType << std::endl;
        pyDeviceSubtype = PyLong_FromUnsignedLong(deviceInfo.deviceSubType);
    }
    PyObject *pySzPortName = PyUnicode_DecodeFSDefault(deviceInfo.szPortName);
    PyObject *pySzDeviceDescription = PyUnicode_DecodeFSDefault(deviceInfo.szDeviceDescription);
    PyObject *pyReserved = PyLong_FromUnsignedLong(deviceInfo.reserved);
    PyObject* pyDeviceInfo(PyDict_New());
    PyDict_SetItemString(pyDeviceInfo, "szPortName", pySzPortName);
    PyDict_SetItemString(pyDeviceInfo, "szDeviceDescription", pySzDeviceDescription);
    PyDict_SetItemString(pyDeviceInfo, "deviceSubType", pyDeviceSubtype);
    PyDict_SetItemString(pyDeviceInfo, "reserved", pyReserved);
    Py_DECREF(pySzPortName);
    Py_DECREF(pySzDeviceDescription);
    Py_DECREF(pyDeviceSubtype);
    Py_DECREF(pyReserved);
    return pyDeviceInfo;
}


PyDoc_STRVAR(PyEds_SetCapacity__doc__,
"Sets the remaining HDD capacity on the host computer\n"
"\t(excluding the portion from image transfer),\n"
"\tas calculated by subtracting the portion from the previous time.\n"
"Set a reset flag initially and designate the cluster length\n"
"\tand number of free clusters.\n"
"Some type 2 protocol standard cameras can display the number of shots\n"
"\tleft on the camera based on the available disk capacity\n"
"\tof the host computer\n"
"For these cameras, after the storage destination is set to the computer,\n"
"\tuse this API to notify the camera of the available disk capacity\n"
"\tof the host computer.\n\n"
":param PyEdsObject camera: The camera object.\n"
":param Dict[str, Any] capacity: The remaining capacity of a transmission place.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SetCapacity(PyObject *Py_UNUSED(self), PyObject *args){
    PyObject* pyCam;
    PyObject* pyCapacity;
    if (!PyArg_ParseTuple(args, "OO!:EdsSetCapacity", &pyCam, &PyDict_Type, &pyCapacity)) {
        return nullptr;
    }

    PyEdsObject* cam(PyToEds(pyCam));
    if (cam == nullptr) {
        return nullptr;
    }

    PyObject* pyNumberOfFreeClusters = PyDict_GetItemString(pyCapacity, "numberOfFreeClusters");
    PyObject* pyBytesPerSector = PyDict_GetItemString(pyCapacity, "bytesPerSector");
    PyObject* pyReset = PyDict_GetItemString(pyCapacity, "reset");
    if (!PyLong_Check(pyNumberOfFreeClusters) || !PyLong_Check(pyBytesPerSector) || !PyBool_Check(pyReset)){
        PyErr_Format(PyExc_ValueError, "Invalid capacity");
        return nullptr;
    }
    EdsCapacity capacity = {
        PyLong_AsLong(pyNumberOfFreeClusters),
        PyLong_AsLong(pyBytesPerSector),
        PyObject_IsTrue(pyReset),
    };
    unsigned long retVal(EdsSetCapacity(cam->edsObj, capacity));
    PyCheck_EDSERROR(retVal);
    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_SendCommand__doc__,
"Sends a command such as \"Shoot\" to a remote camera.\n\n"
":param PyEdsObject camera: The camera object.\n"
":param CameraCommand command: Specifies the command to be sent.\n"
":param int param: Specifies additional command-specific information\n,"
"\tdefaults to 0.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_SendCommand(PyObject *Py_UNUSED(self), PyObject *args){
    PyObject* pyCam;
    unsigned long command;
    long param = 0;
    if (!PyArg_ParseTuple(args, "Okl:EdsSendCommand", &pyCam, &command, &param)) {
        return nullptr;
    }
    PyEdsObject* cam(PyToEds(pyCam));
    if (cam == nullptr) {
        return nullptr;
    }
    unsigned long retVal(EdsSendCommand(cam->edsObj, command, param));
    PyCheck_EDSERROR(retVal);
    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_GetDirectoryItemInfo__doc__,
"Gets information about the directory or file objects\n"
"\ton the memory card (volume) in a remote camera.\n\n"
":param PyEdsObject dir_item: The reference of the directory item.\n"
":raises EdsError: Any of the sdk errors.\n"
":return Dict[str, Any]: Information of the directory item.");

static PyObject* PyEds_GetDirectoryItemInfo(PyObject *Py_UNUSED(self), PyObject *pyDirItem){
    PyEdsObject* dirItem(PyToEds(pyDirItem));
    if (dirItem == nullptr) {
        return nullptr;
    }
    EdsDirectoryItemInfo dirItemInfo;
    unsigned long retVal(EdsGetDirectoryItemInfo(dirItem->edsObj, &dirItemInfo));
    PyCheck_EDSERROR(retVal);

    PyObject *pySize = PyLong_FromUnsignedLongLong(dirItemInfo.size);
    PyObject *pyIsFolder = PyBool_FromLong(dirItemInfo.isFolder);
    PyObject *pyGroupID = PyLong_FromUnsignedLong(dirItemInfo.groupID);
    PyObject *pyOption = PyLong_FromUnsignedLong(dirItemInfo.option);
    PyObject *pySzFileName = PyUnicode_DecodeFSDefault(dirItemInfo.szFileName);
    PyObject *pyFormat = PyLong_FromUnsignedLong(dirItemInfo.format);
    PyObject *pyDateTime = PyLong_FromUnsignedLong(dirItemInfo.dateTime);
    PyObject* pyDirItemInfo(PyDict_New());
    PyDict_SetItemString(pyDirItemInfo, "size", pySize);
    PyDict_SetItemString(pyDirItemInfo, "isFolder", pyIsFolder);
    PyDict_SetItemString(pyDirItemInfo, "groupID", pyGroupID);
    PyDict_SetItemString(pyDirItemInfo, "option", pyOption);
    PyDict_SetItemString(pyDirItemInfo, "szFileName", pySzFileName);
    PyDict_SetItemString(pyDirItemInfo, "format", pyFormat);
    PyDict_SetItemString(pyDirItemInfo, "dateTime", pyDateTime);
    Py_DECREF(pySize);
    Py_DECREF(pyIsFolder);
    Py_DECREF(pyGroupID);
    Py_DECREF(pyOption);
    Py_DECREF(pySzFileName);
    Py_DECREF(pyFormat);
    Py_DECREF(pyDateTime);
    return pyDirItemInfo;
}


PyDoc_STRVAR(PyEds_CreateFileStream__doc__,
"Creates a new file on a host computer (or opens an existing file)\n"
"\tand creates a file stream for access to the file.\n"
"If a new file is designated before executing this API,\n"
"\tthe file is actually created following the timing of writing\n"
"\tby means of EdsWrite or the like with respect to an open stream.\n\n"
":param str filename: the file name.\n"
":param FileCreateDisposition disposition: Action to take on files that exist or not.\n"
":param Access access: Access to the stream (reading, writing, or both).\n"
":raises EdsError: Any of the sdk errors.\n"
":return PyEdsObject: The reference of the stream.");

static PyObject* PyEds_CreateFileStream(PyObject *Py_UNUSED(self), PyObject *args){
    PyObject* pyFilename;
    unsigned long createDisposition;
    unsigned long desiredAccess;

    if (!PyArg_ParseTuple(args, "Okk:CreateFileStream", &pyFilename, &createDisposition, &desiredAccess)) {
        return nullptr;
    }

    if (!PyUnicode_Check(pyFilename) || PyUnicode_GET_LENGTH(pyFilename) == 0) {
        PyErr_SetString(PyExc_TypeError, "filename parameter must be a non-empty string");
        return nullptr;
    }
    PyObject *pyfilenameEncoded(
        PyUnicode_AsEncodedString(pyFilename,
                                  Py_FileSystemDefaultEncoding,
                                  Py_FileSystemDefaultEncodeErrors));
    EdsStreamRef fileStream;
    unsigned long retVal(EdsCreateFileStream(
        PyBytes_AsString(pyfilenameEncoded),
        static_cast<EdsFileCreateDisposition>(createDisposition),
        static_cast<EdsAccess>(desiredAccess),
        &fileStream));

    if (retVal != EDS_ERR_OK) {
        Py_DECREF(pyfilenameEncoded);
        PyCheck_EDSERROR(retVal);
    }
    Py_DECREF(pyfilenameEncoded);
    PyObject *pyFileStream = PyEdsObject_New(fileStream);
    assert(pyFileStream);
    return pyFileStream;
}

PyDoc_STRVAR(PyEds_Download__doc__,
"Downloads a file on a remote camera\n"
"\t(in the camera memory or on a memory card) to the host computer.\n"
"The downloaded file is sent directly to a file stream created in advance.\n"
"When dividing the file being retrieved, call this API repeatedly.\n"
"Also in this case, make the data block size a multiple of 512 (bytes),\n"
"\texcluding the final block.\n\n"
":param PyEdsObject dir_item: The directory item.\n"
":param int size: The number of bytes to be retrieved.\n"
":param PyEdsObject stream: The stream.\n"
":raises EdsError: Any of the sdk errors.");


static PyObject* PyEds_Download(PyObject *Py_UNUSED(self), PyObject *args) {
    PyObject *pyDirItemRef;
    unsigned long long readSize;
    PyObject *pyFileStream;
    if (!PyArg_ParseTuple(args, "OkO:EdsDownload", &pyDirItemRef, &readSize, &pyFileStream)) {
        return nullptr;
    }
    PyEdsObject* dirItem(PyToEds(pyDirItemRef));
    if (dirItem == nullptr) {
        return nullptr;
    }
    PyEdsObject* fileStream(PyToEds(pyFileStream));
    if (fileStream == nullptr) {
        return nullptr;
    }
    unsigned long retVal(EdsDownload(dirItem->edsObj, readSize, fileStream->edsObj));
    PyCheck_EDSERROR(retVal);

    Py_RETURN_NONE;
}


PyDoc_STRVAR(PyEds_DownloadComplete__doc__,
"Must be called when downloading of directory items is complete.\n"
"\tExecuting this API makes the camera\n"
"\t\trecognize that file transmission is complete.\n"
"\tThis operation need not be executed when using EdsDownloadThumbnail.\n\n"
":param PyEdsObject dir_item: The directory item.\n"
":raises EdsError: Any of the sdk errors.");

static PyObject* PyEds_DownloadComplete(PyObject *Py_UNUSED(self), PyObject *pyDirItem){
    PyEdsObject* dirItem(PyToEds(pyDirItem));
    if (dirItem == nullptr) {
        return nullptr;
    }
    unsigned long retVal(EdsDownloadComplete(dirItem->edsObj));
    PyCheck_EDSERROR(retVal);

    Py_RETURN_NONE;
}


PyMethodDef methodTable[] = {
    {"InitializeSDK", (PyCFunction) PyEds_InitializeSDK, METH_NOARGS, PyEds_InitializeSDK__doc__},
    {"TerminateSDK", (PyCFunction) PyEds_TerminateSDK, METH_NOARGS, PyEds_TerminateSDK__doc__},
    {"GetCameraList", (PyCFunction) PyEds_GetCameraList, METH_NOARGS, PyEds_GetCameraList__doc__},
    {"GetChildCount", (PyCFunction) PyEds_GetChildCount, METH_VARARGS, PyEds_GetChildCount__doc__},
    {"GetChildAtIndex", (PyCFunction) PyEds_GetChildAtIndex, METH_VARARGS, PyEds_GetChildAtIndex__doc__},
    {"OpenSession", (PyCFunction) PyEds_OpenSession, METH_VARARGS, PyEds_OpenSession__doc__},
    {"CloseSession", (PyCFunction) PyEds_CloseSession, METH_VARARGS, PyEds_CloseSession__doc__},
    {"GetPropertySize", (PyCFunction) PyEds_GetPropertySize, METH_VARARGS, PyEds_GetPropertySize__doc__},
    {"GetPropertyData", (PyCFunction) PyEds_GetPropertyData, METH_VARARGS, PyEds_GetPropertyData__doc__},
    {"SetPropertyData", (PyCFunction) PyEds_SetPropertyData, METH_VARARGS, PyEds_SetPropertyData__doc__},
    {"GetDeviceInfo", (PyCFunction) PyEds_GetDeviceInfo, METH_O, PyEds_GetDeviceInfo__doc__},
    {"SetCapacity", (PyCFunction) PyEds_SetCapacity, METH_VARARGS, PyEds_SetCapacity__doc__},
    {"SendCommand", (PyCFunction) PyEds_SendCommand, METH_VARARGS, PyEds_SendCommand__doc__},

    {"GetDirectoryItemInfo", (PyCFunction) PyEds_GetDirectoryItemInfo, METH_O, PyEds_GetDirectoryItemInfo__doc__},
    {"CreateFileStream", (PyCFunction) PyEds_CreateFileStream, METH_VARARGS, PyEds_CreateFileStream__doc__},
    {"Download", (PyCFunction) PyEds_Download, METH_VARARGS, PyEds_Download__doc__},
    {"DownloadComplete", (PyCFunction) PyEds_DownloadComplete, METH_O, PyEds_DownloadComplete__doc__},

    {"SetCameraAddedHandler", (PyCFunction) PyEds_SetCameraAddedHandler, METH_VARARGS, PyEds_SetCameraAddedHandler__doc__},
    {"SetCameraStateEventHandler", (PyCFunction) PyEds_SetCameraStateEventHandler, METH_VARARGS, PyEds_SetCameraStateEventHandler__doc__},
    {"SetObjectEventHandler", (PyCFunction) PyEds_SetObjectEventHandler, METH_VARARGS, PyEds_SetObjectEventHandler__doc__},
    {"SetPropertyEventHandler", (PyCFunction) PyEds_SetPropertyEventHandler, METH_VARARGS, PyEds_SetPropertyEventHandler__doc__},

    {nullptr, nullptr, 0, nullptr} // Sentinel value ending the table
};


PyModuleDef edsdkModule = {
    PyModuleDef_HEAD_INIT,
    "api", // Module name
    "Python Wrapper for the Canon EDSDK",
    -1,   // Optional size of the module state memory
    methodTable,
    NULL, // Optional slot definitions
    NULL, // Optional traversal function
    NULL, // Optional clear function
    NULL  // Optional module deallocation function
};

// The module init function
PyMODINIT_FUNC PyInit_api(void) {
    PyEdsObjectType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&PyEdsObjectType) < 0)  {
        return NULL;
    }

    // PyEdsObjectType.tp_name = "edsdk.api.PyEdsObject";
    // PyEdsObjectType.tp_basicsize = sizeof(PyEdsObject);
    // PyEdsObjectType.tp_doc = PyDoc_STR("PyEdsObject object");
    // PyEdsObjectType.tp_new = PyType_GenericNew;
    // // PyEdsObjectType.tp_alloc = PyType_GenericAlloc;
    // PyEdsObjectType.tp_itemsize = 0;
    // PyEdsObjectType.tp_dealloc = (destructor)PyEdsObject_dealloc;
    // PyEdsObjectType.tp_flags = Py_TPFLAGS_DEFAULT;

    PyObject *module = PyModule_Create(&edsdkModule);
    if (module == NULL) {
        return NULL;
    }
    Py_INCREF(&PyEdsObjectType);
    PyModule_AddObject(module, "EdsObject", (PyObject *)&PyEdsObjectType);

    // Import the enums module, where "somepackage.enums"
    // is the full name of the enums module
    PyObject *constants = PyImport_ImportModule("edsdk.constants");
    if (constants == NULL) {
        Py_DECREF(module);
        return nullptr;
    }
    Py_DECREF(constants);

    PyEdsError = PyErr_NewException("edsdk.EdsError", NULL, NULL);
    Py_XINCREF(PyEdsError);

    if (PyModule_AddObject(module, "EdsError", PyEdsError) < 0) {
        Py_XDECREF(PyEdsError);
        Py_CLEAR(PyEdsError);
        Py_DECREF(module);
        return nullptr;
    }

    PyTypeObject *pyEdsError_type = (PyTypeObject *)PyEdsError;
    pyEdsError_type->tp_str = PyEdsError_tp_str;

	PyObject *pyEdsErrorDescr = PyDescr_NewGetSet(pyEdsError_type, PyEdsError_getsetters);
	if (PyDict_SetItem(pyEdsError_type->tp_dict, PyDescr_NAME(pyEdsErrorDescr), pyEdsErrorDescr) < 0) {
        Py_DECREF(PyEdsError);
        Py_CLEAR(PyEdsError);
		Py_DECREF(pyEdsErrorDescr);
		Py_DECREF(module);
		return nullptr;
	}
	Py_DECREF(pyEdsErrorDescr);

    if (!PyEval_ThreadsInitialized()) {
        PyEval_InitThreads();
    }

    return module;
};
