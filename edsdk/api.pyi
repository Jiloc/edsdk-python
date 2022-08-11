from typing import Tuple, Dict, Callable, Any

from edsdk.constants import StateEvent, ObjectEvent, PropertyEvent, PropID, CameraCommand, Access, FileCreateDisposition, DataType


class EdsObject:
    ...


def InitializeSDK() -> None:
    """Initializes the libraries
    When using the EDSDK libraries, you must call this API once
        before using EDSDK APIs

    :raises EdsError: Any of the sdk errors.
    """
    ...


def TerminateSDK() -> None:
    """Terminates use of the libraries
    This function muse be called when ending the SDK.
    Calling this function releases all resources allocated by the libraries.

    :raises EdsError: Any of the sdk errors.
    """
    ...


def GetCameraList() -> EdsObject:
    """Gets camera list objects.

    :raises EdsError: Any of the sdk errors.
    :return EdsObject: the camera-list.
    """
    ...


def GetChildCount(parent: EdsObject) -> int:
    """Gets the number of child objects of the designated object.
    Example: Number of files in a directory

    :param EdsObject parent: the list object.
    :raises EdsError: Any of the sdk errors.
    :return int: Number of elements in this list.
    """
    ...


def GetChildAtIndex(parent: EdsObject, index: int) -> EdsObject:
    """Gets an indexed child object of the designated object

    :param EdsObject parent: the list object.
    :param int index: The index that is passed in, is zero based.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: the child object.
    """
    ...


def OpenSession(camera: EdsObject) -> None:
    """Establishes a logical connection with a remote camera.
    Use this API after getting the camera's EdsCamera object.

    :param EdsObject camera: the camera.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def CloseSession(camera: EdsObject) -> None:
    """Closes a logical connection with a remote camera

    :param EdsObject camera: the camera.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def SetCameraAddedHandler(callback: Callable) -> None:
    """Registers a callback function for when a camera is detected.

    :param Callable callback: the callback called when a camera is connected.
        Expected signature () -> int.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def SetCameraStateEventHandler(camera: EdsObject, event: StateEvent, callback: Callable) -> None:
    """Registers a callback function for receiving status
            change notification events for property states on a camera

    :param EdsObject camera: the camera object.
    :param StateEvent event: the event to be supplemented.
        To designate all events, use StateEvent.All.
    :param Callable callback: the callback for receiving the events.
        Expected signature (event: StateEvent, event_data: int) -> int.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def SetObjectEventHandler(camera: EdsObject, event: ObjectEvent, callback: Callable) -> None:
    """Registers a callback function for receiving status
            change notification events for objects on a remote camera.
    Here, object means volumes representing memory cards, files and directories,
        tand shot images stored in memory, in particular.

    :param EdsObject camera: the camera object.
    :param ObjectEvent event: the event to be supplemented.
        To designate all events, use ObjectEvent.All.
    :param Callable callback: the callback for receiving events.
        Expected signature (event: ObjectEvent, obj_ref: EdsObject) -> int.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def SetPropertyEventHandler(camera: EdsObject, event: PropertyEvent, callback: Callable) -> None:
    """Registers a callback function for receiving status
            change notification events for property states on a camera.

    :param EdsObject camera: the camera object.
    :param PropertyEvent event: the event to be supplemented.
        To designate all events, use PropertyEvent.All.
    :param Callable callback: the callback for receiving events.
        Expected signature (event: StateEvent, prop_id: PropID, param: int) -> int.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def GetPropertySize(camera_or_image: EdsObject, property_id: PropID, param: int = 0) -> Tuple[DataType, int]:
    """Gets the byte size and data type of a designated property
            from a camera object or image object.

    :param EdsObject camera_or_image: the item object.
    :param PropID property_id: The property ID.
    :param int param: Specify an index in case there are two or
        more values over the same ID, defaults to 0.
    :raises EdsError: Any of the sdk errors.
    :return Tuple[DataType, int]: the property DataType and size in bytes.
    """
    ...


def GetPropertyData(camera_or_image: EdsObject, property_id: PropID, param: int = 0) -> Any:
    """Gets property information from the designated object.

    :param EdsObject camera_or_image: The reference of the item.
    :param PropID property_id: The PropertyID.
    :param int param: Specify an index in case there are two or
        more values over the same ID, defaults to 0.
    :raises EdsError: Any of the sdk errors.
    :return Any: The property value.
    """
    ...


def SetPropertyData(camera_or_image: EdsObject, property_id: PropID, param: int, data: Any) -> None:
    """Sets property data for the designated object.

    :param EdsObject camera_or_image: The item object.
    :param PropID property_id: The PropertyID.
    :param int param: Specify an index in case there are two or
        more values over the same ID.
    :param Any data: The data to set.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def GetDeviceInfo(camera: EdsObject) -> Dict[str, Any]:
    """Gets device information, such as the device name.
    Because device information of remote cameras is stored
        on the host computer, you can use this API
        before the camera object initiates communication
        (that is, before a session is opened).

    :param EdsObject camera: The camera object.
    :raises EdsError: Any of the sdk errors.
    :return Dict[str, Any]: The device information.
    """
    ...


def SetCapacity(camera: EdsObject, capacity: Dict[str, Any]) -> None:
    """Sets the remaining HDD capacity on the host computer
            (excluding the portion from image transfer),
            as calculated by subtracting the portion from the previous time.
    Set a reset flag initially and designate the cluster length
        and number of free clusters.
    Some type 2 protocol standard cameras can display the number of shots
        left on the camera based on the available disk capacity
        of the host computer
    For these cameras, after the storage destination is set to the computer,
        use this API to notify the camera of the available disk capacity
        of the host computer.

    :param EdsObject camera: The camera object.
    :param Dict[str, Any] capacity: The remaining capacity of a transmission place.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def SendCommand(camera: EdsObject, command: CameraCommand, param: int = 0) -> None:
    """Sends a command such as "Shoot" to a remote camera.

    :param EdsObject camera: The camera object.
    :param CameraCommand command: Specifies the command to be sent.
    :param int param: Specifies additional command-specific information,
        defaults to 0.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def GetDirectoryItemInfo(dir_item: EdsObject) -> Dict[str, Any]:
    """Gets information about the directory or file objects
            on the memory card (volume) in a remote camera.

    :param EdsObject dir_item: The reference of the directory item.
    :raises EdsError: Any of the sdk errors.
    :return Dict[str, Any]: Information of the directory item.
    """
    ...


def CreateFileStream(filename: str, disposition: FileCreateDisposition, access: Access) -> EdsObject:
    """Creates a new file on a host computer (or opens an existing file)
            and creates a file stream for access to the file.
    If a new file is designated before executing this API,
        the file is actually created following the timing of writing
        by means of EdsWrite or the like with respect to an open stream.

    :param str filename: the file name.
    :param FileCreateDisposition disposition: Action to take on files that exist or not.
    :param Access access: Access to the stream (reading, writing, or both).
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The reference of the stream.
    """
    ...


def Download(dir_item: EdsObject, size: int, stream: EdsObject) -> None:
    """Downloads a file on a remote camera
            (in the camera memory or on a memory card) to the host computer.
    The downloaded file is sent directly to a file stream created in advance.
    When dividing the file being retrieved, call this API repeatedly.
    Also in this case, make the data block size a multiple of 512 (bytes),
        excluding the final block.
    :param EdsObject dir_item: The directory item.
    :param int size: The number of bytes to be retrieved.
    :param EdsObject stream: The stream.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def DownloadComplete(dir_item: EdsObject) -> None:
    """Must be called when downloading of directory items is complete.
            Executing this API makes the camera
                recognize that file transmission is complete.
            This operation need not be executed when using EdsDownloadThumbnail.

    :param EdsObject dir_item: The directory item.
    :raises EdsError: Any of the sdk errors.
    """
    ...
