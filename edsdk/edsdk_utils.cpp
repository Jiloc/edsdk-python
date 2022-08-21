#include "edsdk_utils.h"

#include <string>
#include <map>

#include "EDSDKErrors.h"


namespace EDS {
    char const *errorMessage(EdsError const error) {
        static std::map<EdsError const, char const *> const errorMap = {
            /*-----------------------------------------------------------------------
            ED-SDK Error Code Masks
            ------------------------------------------------------------------------*/
            {0x80000000UL, "EDS_ISSPECIFIC_MASK"},
            {0x7F000000L, "EDS_COMPONENTID_MASK"},
            {0x00FF0000L, "EDS_RESERVED_MASK"},
            {0x0000FFFFL, "EDS_ERRORID_MASK"},

            /*-----------------------------------------------------------------------
            ED-SDK Base Component IDs
            ------------------------------------------------------------------------*/
            {0x01000000L, "EDS_CMP_ID_CLIENT_COMPONENTID"},
            {0x02000000L, "EDS_CMP_ID_LLSDK_COMPONENTID"},
            {0x03000000L, "EDS_CMP_ID_HLSDK_COMPONENTID"},

            /*-----------------------------------------------------------------------
            ED-SDK Functin Success Code
            ------------------------------------------------------------------------*/
            {0x00000000L, "EDS_ERR_OK"},

            /*-----------------------------------------------------------------------
            ED-SDK Generic Error IDs
            ------------------------------------------------------------------------*/
            /* Miscellaneous errors */
            {0x00000001L, "EDS_ERR_UNIMPLEMENTED"},
            {0x00000002L, "EDS_ERR_INTERNAL_ERROR"},
            {0x00000003L, "EDS_ERR_MEM_ALLOC_FAILED"},
            {0x00000004L, "EDS_ERR_MEM_FREE_FAILED"},
            {0x00000005L, "EDS_ERR_OPERATION_CANCELLED"},
            {0x00000006L, "EDS_ERR_INCOMPATIBLE_VERSION"},
            {0x00000007L, "EDS_ERR_NOT_SUPPORTED"},
            {0x00000008L, "EDS_ERR_UNEXPECTED_EXCEPTION"},
            {0x00000009L, "EDS_ERR_PROTECTION_VIOLATION"},
            {0x0000000AL, "EDS_ERR_MISSING_SUBCOMPONENT"},
            {0x0000000BL, "EDS_ERR_SELECTION_UNAVAILABLE"},

            /* File errors */
            {0x00000020L, "EDS_ERR_FILE_IO_ERROR"},
            {0x00000021L, "EDS_ERR_FILE_TOO_MANY_OPEN"},
            {0x00000022L, "EDS_ERR_FILE_NOT_FOUND"},
            {0x00000023L, "EDS_ERR_FILE_OPEN_ERROR"},
            {0x00000024L, "EDS_ERR_FILE_CLOSE_ERROR"},
            {0x00000025L, "EDS_ERR_FILE_SEEK_ERROR"},
            {0x00000026L, "EDS_ERR_FILE_TELL_ERROR"},
            {0x00000027L, "EDS_ERR_FILE_READ_ERROR"},
            {0x00000028L, "EDS_ERR_FILE_WRITE_ERROR"},
            {0x00000029L, "EDS_ERR_FILE_PERMISSION_ERROR"},
            {0x0000002AL, "EDS_ERR_FILE_DISK_FULL_ERROR"},
            {0x0000002BL, "EDS_ERR_FILE_ALREADY_EXISTS"},
            {0x0000002CL, "EDS_ERR_FILE_FORMAT_UNRECOGNIZED"},
            {0x0000002DL, "EDS_ERR_FILE_DATA_CORRUPT"},
            {0x0000002EL, "EDS_ERR_FILE_NAMING_NA"},

            /* Directory errors */
            {0x00000040L, "EDS_ERR_DIR_NOT_FOUND"},
            {0x00000041L, "EDS_ERR_DIR_IO_ERROR"},
            {0x00000042L, "EDS_ERR_DIR_ENTRY_NOT_FOUND"},
            {0x00000043L, "EDS_ERR_DIR_ENTRY_EXISTS"},
            {0x00000044L, "EDS_ERR_DIR_NOT_EMPTY"},

            /* Property errors */
            {0x00000050L, "EDS_ERR_PROPERTIES_UNAVAILABLE"},
            {0x00000051L, "EDS_ERR_PROPERTIES_MISMATCH"},
            {0x00000053L, "EDS_ERR_PROPERTIES_NOT_LOADED"},

            /* Function Parameter errors */
            {0x00000060L, "EDS_ERR_INVALID_PARAMETER"},
            {0x00000061L, "EDS_ERR_INVALID_HANDLE"},
            {0x00000062L, "EDS_ERR_INVALID_POINTER"},
            {0x00000063L, "EDS_ERR_INVALID_INDEX"},
            {0x00000064L, "EDS_ERR_INVALID_LENGTH"},
            {0x00000065L, "EDS_ERR_INVALID_FN_POINTER"},
            {0x00000066L, "EDS_ERR_INVALID_SORT_FN"},

            /* Device errors */
            {0x00000080L, "EDS_ERR_DEVICE_NOT_FOUND"},
            {0x00000081L, "EDS_ERR_DEVICE_BUSY. Note: If a device busy error occurs, reissue the command after a while. The camera will become unstable."},
            {0x00000082L, "EDS_ERR_DEVICE_INVALID"},
            {0x00000083L, "EDS_ERR_DEVICE_EMERGENCY"},
            {0x00000084L, "EDS_ERR_DEVICE_MEMORY_FULL"},
            {0x00000085L, "EDS_ERR_DEVICE_INTERNAL_ERROR"},
            {0x00000086L, "EDS_ERR_DEVICE_INVALID_PARAMETER"},
            {0x00000087L, "EDS_ERR_DEVICE_NO_DISK"},
            {0x00000088L, "EDS_ERR_DEVICE_DISK_ERROR"},
            {0x00000089L, "EDS_ERR_DEVICE_CF_GATE_CHANGED"},
            {0x0000008AL, "EDS_ERR_DEVICE_DIAL_CHANGED"},
            {0x0000008BL, "EDS_ERR_DEVICE_NOT_INSTALLED"},
            {0x0000008CL, "EDS_ERR_DEVICE_STAY_AWAKE"},
            {0x0000008DL, "EDS_ERR_DEVICE_NOT_RELEASED"},

            /* Stream errors */
            {0x000000A0L, "EDS_ERR_STREAM_IO_ERROR"},
            {0x000000A1L, "EDS_ERR_STREAM_NOT_OPEN"},
            {0x000000A2L, "EDS_ERR_STREAM_ALREADY_OPEN"},
            {0x000000A3L, "EDS_ERR_STREAM_OPEN_ERROR"},
            {0x000000A4L, "EDS_ERR_STREAM_CLOSE_ERROR"},
            {0x000000A5L, "EDS_ERR_STREAM_SEEK_ERROR"},
            {0x000000A6L, "EDS_ERR_STREAM_TELL_ERROR"},
            {0x000000A7L, "EDS_ERR_STREAM_READ_ERROR"},
            {0x000000A8L, "EDS_ERR_STREAM_WRITE_ERROR"},
            {0x000000A9L, "EDS_ERR_STREAM_PERMISSION_ERROR"},
            {0x000000AAL, "EDS_ERR_STREAM_COULDNT_BEGIN_THREAD. Could not start reading thumbnail"},
            {0x000000ABL, "EDS_ERR_STREAM_BAD_OPTIONS"},
            {0x000000ACL, "EDS_ERR_STREAM_END_OF_STREAM"},

            /* Communications errors */
            {0x000000C0L, "EDS_ERR_COMM_PORT_IS_IN_USE"},
            {0x000000C1L, "EDS_ERR_COMM_DISCONNECTED"},
            {0x000000C2L, "EDS_ERR_COMM_DEVICE_INCOMPATIBLE"},
            {0x000000C3L, "EDS_ERR_COMM_BUFFER_FULL"},
            {0x000000C4L, "EDS_ERR_COMM_USB_BUS_ERR"},

            /* Lock/Unlock */
            {0x000000D0L, "EDS_ERR_USB_DEVICE_LOCK_ERROR"},
            {0x000000D1L, "EDS_ERR_USB_DEVICE_UNLOCK_ERROR"},

            /* STI/WIA */
            {0x000000E0L, "EDS_ERR_STI_UNKNOWN_ERROR"},
            {0x000000E1L, "EDS_ERR_STI_INTERNAL_ERROR"},
            {0x000000E2L, "EDS_ERR_STI_DEVICE_CREATE_ERROR"},
            {0x000000E3L, "EDS_ERR_STI_DEVICE_RELEASE_ERROR"},
            {0x000000E4L, "EDS_ERR_DEVICE_NOT_LAUNCHED"},

            {0x000000F0L, "EDS_ERR_ENUM_NA. Enumeration terminated (there was no suitable enumeration item)"},
            {0x000000F1L, "EDS_ERR_INVALID_FN_CALL. Called in a mode when the function could not be used"},
            {0x000000F2L, "EDS_ERR_HANDLE_NOT_FOUND"},
            {0x000000F3L, "EDS_ERR_INVALID_ID"},
            {0x000000F4L, "EDS_ERR_WAIT_TIMEOUT_ERROR"},

            /* PTP */
            {0x00002003, "EDS_ERR_SESSION_NOT_OPEN"},
            {0x00002004, "EDS_ERR_INVALID_TRANSACTIONID"},
            {0x00002007, "EDS_ERR_INCOMPLETE_TRANSFER"},
            {0x00002008, "EDS_ERR_INVALID_STRAGEID. Storage error"},
            {0x0000200A, "EDS_ERR_DEVICEPROP_NOT_SUPPORTED"},
            {0x0000200B, "EDS_ERR_INVALID_OBJECTFORMATCODE"},
            {0x00002011, "EDS_ERR_SELF_TEST_FAILED"},
            {0x00002012, "EDS_ERR_PARTIAL_DELETION"},
            {0x00002014, "EDS_ERR_SPECIFICATION_BY_FORMAT_UNSUPPORTED"},
            {0x00002015, "EDS_ERR_NO_VALID_OBJECTINFO"},
            {0x00002016, "EDS_ERR_INVALID_CODE_FORMAT"},
            {0x00002017, "EDS_ERR_UNKNOWN_VENDOR_CODE"},
            {0x00002018, "EDS_ERR_CAPTURE_ALREADY_TERMINATED"},
            {0x00002019, "EDS_ERR_PTP_DEVICE_BUSY"},
            {0x0000201A, "EDS_ERR_INVALID_PARENTOBJECT"},
            {0x0000201B, "EDS_ERR_INVALID_DEVICEPROP_FORMAT"},
            {0x0000201C, "EDS_ERR_INVALID_DEVICEPROP_VALUE"},
            {0x0000201E, "EDS_ERR_SESSION_ALREADY_OPEN"},
            {0x0000201F, "EDS_ERR_TRANSACTION_CANCELLED"},
            {0x00002020, "EDS_ERR_SPECIFICATION_OF_DESTINATION_UNSUPPORTED"},
            {0x00002021, "EDS_ERR_NOT_CAMERA_SUPPORT_SDK_VERSION"},

            /* PTP Vendor */
            {0x0000A001, "EDS_ERR_UNKNOWN_COMMAND"},
            {0x0000A005, "EDS_ERR_OPERATION_REFUSED"},
            {0x0000A006, "EDS_ERR_LENS_COVER_CLOSE"},
            {0x0000A101, "EDS_ERR_LOW_BATTERY"},
            {0x0000A102, "EDS_ERR_OBJECT_NOTREADY. Image data set not ready for live view"},
            {0x0000A104, "EDS_ERR_CANNOT_MAKE_OBJECT"},
            {0x0000A106, "EDS_ERR_MEMORYSTATUS_NOTREADY"},

            /* Take Picture errors */
            {0x00008D01L, "EDS_ERR_TAKE_PICTURE_AF_NG. Focus Failed"},
            {0x00008D02L, "EDS_ERR_TAKE_PICTURE_RESERVED"},
            {0x00008D03L, "EDS_ERR_TAKE_PICTURE_MIRROR_UP_NG. Currently configuring mirror up"},
            {0x00008D04L, "EDS_ERR_TAKE_PICTURE_SENSOR_CLEANING_NG"},
            {0x00008D05L, "EDS_ERR_TAKE_PICTURE_SILENCE_NG. Currently performing silent operations"},
            {0x00008D06L, "EDS_ERR_TAKE_PICTURE_NO_CARD_NG"},
            {0x00008D07L, "EDS_ERR_TAKE_PICTURE_CARD_NG. Error writing to card"},
            {0x00008D08L, "EDS_ERR_TAKE_PICTURE_CARD_PROTECT_NG. Card write protected"},
            {0x00008D09L, "EDS_ERR_TAKE_PICTURE_MOVIE_CROP_NG"},
            {0x00008D0AL, "EDS_ERR_TAKE_PICTURE_STROBO_CHARGE_NG. Faild in flash off"},
            {0x00008D0BL, "EDS_ERR_TAKE_PICTURE_NO_LENS_NG. Lens is not attached"},
            {0x00008D0CL, "EDS_ERR_TAKE_PICTURE_SPECIAL_MOVIE_MODE_NG. Movie camera exceeds the limit"},
            {0x00008D0DL, "EDS_ERR_TAKE_PICTURE_LV_REL_PROHIBIT_MODE_NG. Faild in live view preparing taking picture for changing AEmode(Candlelight only)"},
            {0x00008D0EL, "EDS_ERR_TAKE_PICTURE_MOVIE_MODE_NG. Faild in taking still image with getting ready for movie mode"},
            {0x00008D0FL, "EDS_ERR_TAKE_PICTURE_RETRUCTED_LENS_NG. Retructed lens is retracted"},


            {0x000000F5L, "EDS_ERR_LAST_GENERIC_ERROR_PLUS_ONE"},
        };

        std::map<EdsError const, char const *>::const_iterator it = errorMap.find(error);
        return it == errorMap.end() ? "Unknown error" : it->second;
    }


    PyObject *PyDict_FromEdsPoint(EdsPoint const &point) {
        PyObject *pyDict(PyDict_New());
        PyObject *pyX(PyLong_FromLong(point.x));
        PyObject *pyY(PyLong_FromLong(point.y));
        PyDict_SetItemString(pyDict, "x", pyX);
        PyDict_SetItemString(pyDict, "y", pyY);
        Py_DECREF(pyX);
        Py_DECREF(pyY);
        return pyDict;
    }


    PyObject *PyDict_FromEdsSize(EdsSize const &size) {
        PyObject *pyDict(PyDict_New());
        PyObject *pyWidth(PyLong_FromLong(size.width));
        PyObject *pyHeight(PyLong_FromLong(size.height));
        PyDict_SetItemString(pyDict, "width", pyWidth);
        PyDict_SetItemString(pyDict, "height", pyHeight);
        Py_DECREF(pyWidth);
        Py_DECREF(pyHeight);
        return pyDict;
    }


    PyObject *PyDict_FromEdsRect(EdsRect const &rect) {
        PyObject *pyDict(PyDict_New());
        PyObject *pyPoint(PyDict_FromEdsPoint(rect.point));
        PyObject *pySize(PyDict_FromEdsSize(rect.size));
        PyDict_SetItemString(pyDict, "point", pyPoint);
        PyDict_SetItemString(pyDict, "size", pySize);
        Py_DECREF(pyPoint);
        Py_DECREF(pySize);
        return pyDict;
    }


    PyObject *PyDict_FromEdsImageInfo(EdsImageInfo const &imageInfo) {
        PyObject *pyWidth(PyLong_FromUnsignedLong(imageInfo.width));
        PyObject *pyHeight(PyLong_FromUnsignedLong(imageInfo.height));
        PyObject *pyNumOfComponents(PyLong_FromUnsignedLong(imageInfo.numOfComponents));
        PyObject *pyComponentDepth(PyLong_FromUnsignedLong(imageInfo.componentDepth));
        PyObject *pyEffectiveRect(PyDict_FromEdsRect(imageInfo.effectiveRect));
        PyObject *pyReserved1(PyLong_FromUnsignedLong(imageInfo.reserved1));
        PyObject *pyReserved2(PyLong_FromUnsignedLong(imageInfo.reserved2));

        PyObject* pyImageInfo(PyDict_New());
        PyDict_SetItemString(pyImageInfo, "width", pyWidth);
        PyDict_SetItemString(pyImageInfo, "height", pyHeight);
        PyDict_SetItemString(pyImageInfo, "numOfComponents", pyNumOfComponents);
        PyDict_SetItemString(pyImageInfo, "componentDepth", pyComponentDepth);
        PyDict_SetItemString(pyImageInfo, "effectiveRect", pyEffectiveRect);
        PyDict_SetItemString(pyImageInfo, "reserved1", pyReserved1);
        PyDict_SetItemString(pyImageInfo, "reserved2", pyReserved2);

        Py_DECREF(pyWidth);
        Py_DECREF(pyHeight);
        Py_DECREF(pyNumOfComponents);
        Py_DECREF(pyComponentDepth);
        Py_DECREF(pyEffectiveRect);
        Py_DECREF(pyReserved1);
        Py_DECREF(pyReserved2);
        return pyImageInfo;
    }


    bool PyDict_ToEdsPoint(PyObject *pyDict, EdsPoint &point) {
        // Check if the dictionary has the correct keys
        PyObject *pyX(PyDict_GetItemString(pyDict, "width"));
        PyObject *pyY(PyDict_GetItemString(pyDict, "height"));

        if (!pyX || !pyY || !PyLong_Check(pyX) || !PyLong_Check(pyY)) {
            PyErr_SetString(
                PyExc_TypeError,
                "Invalid EdsPoint, expected {\"x\": int, \"y\": int)");
            return false;
        }
        point.x = PyLong_AsLong(pyX);
        point.y = PyLong_AsLong(pyY);
        return true;
    }


    bool PyDict_ToEdsSize(PyObject *pyDict, EdsSize &size) {
        PyObject *pyWidth(PyDict_GetItemString(pyDict, "width"));
        PyObject *pyHeight(PyDict_GetItemString(pyDict, "height"));

        if (!pyWidth || !pyHeight || !PyLong_Check(pyWidth) || !PyLong_Check(pyHeight)){
            PyErr_SetString(
                PyExc_TypeError,
                "Invalid EdsSize, expected {\"width\": int, \"height\": int)");
            return false;
        }
        size.width = PyLong_AsLong(pyWidth);
        size.height = PyLong_AsLong(pyHeight);
        return true;
    }


    bool PyDict_ToEdsRect(PyObject *pyDict, EdsRect &rect) {
        PyObject *pyPoint(PyDict_GetItemString(pyDict, "point"));
        PyObject *pySize(PyDict_GetItemString(pyDict, "size"));

        if (!PyDict_Check(pyPoint) || !PyDict_Check(pySize)){
            PyErr_SetString(
                PyExc_TypeError,
                "Invalid EdsRect, expected {"
                "\"point\": {\"x\": int, \"y\": int}, "
                "\"size\": {\"width\": int, \"height\": int}}");
            return false;
        }
        return PyDict_ToEdsPoint(pyDict, rect.point) &&
               PyDict_ToEdsSize(pyDict, rect.size);
    }
}
