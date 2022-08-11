import os
import time
import uuid
from typing import Callable, Tuple, Any


import edsdk
from edsdk import CameraCommand, ObjectEvent, PropID, PropertyEvent, FileCreateDisposition, Access, SaveTo, EdsObject

if os.name == 'nt':
    # If you're using the EDSDK on Windows,
    # you have to have a Windows message loop in your main thread,
    # otherwise callbacks won't happen.
    # (This is because the EDSDK uses the obsolete COM STA threading model
    # instead of real threads.)
    import pythoncom

    def win_wrapper(func: Callable) -> Callable:
        def wrapped(*args):
            ret = func(*args)
            pythoncom.PumpWaitingMessages()
            return ret
        return wrapped

    for func_name in dir(edsdk.api):
        func = getattr(edsdk.api, func_name)
        if not func_name.startswith("_") and callable(func):
            setattr(edsdk.api, func_name, win_wrapper(func))


def save_image(object_handle: EdsObject, save_to: str) -> int:
    dir_item_info = edsdk.GetDirectoryItemInfo(object_handle)
    out_stream = edsdk.CreateFileStream(
        os.path.join(save_to, str(uuid.uuid4()) + ".raw"),
        FileCreateDisposition.CreateAlways,
        Access.ReadWrite)
    edsdk.Download(object_handle, dir_item_info["size"], out_stream)
    edsdk.DownloadComplete(object_handle)
    return 0


def callback_property(event: PropertyEvent, property_id: PropID, parameter: int) -> int:
    print("event: ", event)
    print("Property changed:", property_id)
    print("Parameter:", parameter)
    return 0


def callback_object(event: ObjectEvent, object_handle: EdsObject) -> int:
    print("event: ", event, "object_handle:", object_handle)
    if event == ObjectEvent.DirItemRequestTransfer:
        save_image(object_handle, ".")
    return 0


if __name__ == '__main__':
    edsdk.InitializeSDK()
    cam_list = edsdk.GetCameraList()
    nr_cameras = edsdk.GetChildCount(cam_list)

    if nr_cameras == 0:
        print("No cameras connected")
        exit(1)

    cam = edsdk.GetChildAtIndex(cam_list, 0)
    print(cam)
    edsdk.OpenSession(cam)
    # edsdk.SetPropertyEventHandler(cam, PropertyEvent.All, callback_property)
    edsdk.SetObjectEventHandler(cam, ObjectEvent.All, callback_object)
    edsdk.SetPropertyData(cam, PropID.SaveTo, 0, SaveTo.Host)
    print(edsdk.GetPropertyData(cam, PropID.SaveTo, 0))
    # Sets HD Capacity to an arbitrary big value
    edsdk.SetCapacity(cam, {"reset": True, "bytesPerSector": 512, "numberOfFreeClusters": 2147483647})
    print(edsdk.GetDeviceInfo(cam))
    edsdk.SendCommand(cam, CameraCommand.TakePicture, 0)
    time.sleep(5)
    if os.name == 'nt':
        pythoncom.PumpWaitingMessages()

    edsdk.TerminateSDK()

    # StopEvent = win32event.CreateEvent(None, 0, 0, None)
    # OtherEvent = win32event.CreateEvent(None, 0, 0, None)
    # # _MessagePump()
    # pythoncom.EnableQuitMessage(t.native_id)
