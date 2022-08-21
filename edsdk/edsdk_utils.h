#include <Python.h>

#include <map>

#include "EDSDKTypes.h"


#define PyCheck_EDSERROR(err) \
    if (err != EDS_ERR_OK) { \
    	PyObject *exc_args = PyTuple_New(2); \
	    PyTuple_SetItem(exc_args, 0, PyUnicode_FromString(EDS::errorMessage(err))); \
	    PyTuple_SetItem(exc_args, 1, PyLong_FromLong(err)); \
	    PyErr_SetObject(PyEdsError, exc_args); \
        return nullptr; \
    }


namespace EDS {
    char const *errorMessage(EdsError const error);

    PyObject *PyDict_FromEdsPoint(EdsPoint const &point);
    PyObject *PyDict_FromEdsSize(EdsSize const &size);
    PyObject *PyDict_FromEdsRect(EdsRect const &rect);
    PyObject *PyDict_FromEdsImageInfo(EdsImageInfo const &imageInfo);

    bool PyDict_ToEdsPoint(PyObject *pyDict, EdsPoint &point);
    bool PyDict_ToEdsSize(PyObject *pyDict, EdsSize &size);
    bool PyDict_ToEdsRect(PyObject *pyDict, EdsRect &rect);

    std::map<EdsDataType const, std::size_t const> const DataTypeSize = {
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
}
