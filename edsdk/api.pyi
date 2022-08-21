from typing import Tuple, Dict, Callable, Any, Union
from edsdk.constants import (
    CameraStatusCommand,
    ProgressOption,
    StateEvent,
    ObjectEvent,
    PropertyEvent,
    PropID,
    CameraCommand,
    Access,
    FileCreateDisposition,
    DataType,
    ImageSource,
    TargetImageType,
)


class EdsObject: ...


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


def GetParent(item: EdsObject) -> EdsObject:
    """Gets the parent object of the designated object.

    :param EdsObject item: the item object.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: the parent object.
    """
    ...


def GetPropertySize(
    camera_or_image: EdsObject, property_id: PropID, param: int = 0
) -> Tuple[DataType, int]:
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


def GetPropertyData(
    camera_or_image: EdsObject, property_id: PropID, param: int = 0
) -> Any:
    """Gets property information from the designated object.

    :param EdsObject camera_or_image: The reference of the item.
    :param PropID property_id: The PropertyID.
    :param int param: Specify an index in case there are two or
        more values over the same ID, defaults to 0.
    :raises EdsError: Any of the sdk errors.
    :return Any: The property value.
    """
    ...


def SetPropertyData(
    camera_or_image: EdsObject, property_id: PropID, param: int, data: Any
) -> None:
    """Sets property data for the designated object.

    :param EdsObject camera_or_image: The item object.
    :param PropID property_id: The PropertyID.
    :param int param: Specify an index in case there are two or
        more values over the same ID.
    :param Any data: The data to set.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def GetPropertyDesc(camera: EdsObject, property_id: PropID) -> Dict[str, Any]:
    """Gets a list of property data that can be set for the object
        designated in inRef, as well as maximum and minimum values.
    This API is intended for only some shooting-related properties.


    :param EdsObject camera: The camera item.
    :param PropID property_id: The Property ID.
    :raises EdsError: Any of the sdk errors.
    :return Dict[str, Any]: The values which can be set up.
    """
    ...


def GetCameraList() -> EdsObject:
    """Gets camera list objects.

    :raises EdsError: Any of the sdk errors.
    :return EdsObject: the camera-list.
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


def SendCommand(camera: EdsObject, command: CameraCommand, param: int = 0) -> None:
    """Sends a command such as "Shoot" to a remote camera.

    :param EdsObject camera: The camera object.
    :param CameraCommand command: Specifies the command to be sent.
    :param int param: Specifies additional command-specific information,
        defaults to 0.
    :raises EdsError: Any of the sdk errors.
    """
    ...

def SendStatusCommand(
    camera: EdsObject, command: CameraStatusCommand, param: int = 0
) -> None:
    """Sends a command such as "Shoot" to a remote camera.

    :param EdsObject camera: The camera object.
    :param CameraStatusCommand command: Specifies the command to be sent.
    :param int param: Specifies additional command-specific information,
        defaults to 0.
    :raises EdsError: Any of the sdk errors.
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


def GetVolumeInfo(volume: EdsObject) -> Dict[str, Any]:
    """Gets volume information for a memory card in the camera.

    :param EdsObject volume: The volume item.
    :raises EdsError: Any of the sdk errors.
    :return Dict[str, Any]: Information of the volume
    """
    ...


def FormatVolume(volume: EdsObject) -> None:
    """Formats volumes of memory cards in a camera.

    :param EdsObject volume: The volume item.
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


def DeleteDirectoryItem(dir_item: EdsObject) -> None:
    """Deletes a camera folder or file.
    If folders with subdirectories are designated, all files are deleted
        except protected files.
    EdsDirectoryItem objects deleted by means of this API are implicitly
        released by the EDSDK.

    :param EdsObject dir_item: The item to be deleted.
    :raises EdsError: Any of the sdk errors.
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


def DownloadCancel(dir_item: EdsObject) -> None:
    """Must be executed when downloading of a directory item is canceled.
    Calling this API makes the camera cancel file transmission.
    It also releases resources.
    This operation need not be executed when using EdsDownloadThumbnail.

    :param EdsObject dir_item: The directory item.
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


def DownloadThumbnail(dir_item: EdsObject) -> EdsObject:
    """Extracts and downloads thumbnail information from image files in a camera.
    Thumbnail information in the camera's image files is downloaded
        to the host computer.
    Downloaded thumbnails are sent directly to a file stream created in advance.

    :param EdsObject dir_item: The directory item.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The stream.
    """
    ...


def GetAttribute(dir_item: EdsObject) -> int:
    """Gets attributes of files on a camera.

    :param EdsObject dir_item: The directory item.
    :raises EdsError: Any of the sdk errors.
    :return int: Indicates the file attributes.
        As for the file attributes, OR values of the value defined
        by enum FileAttributes can be retrieved. Thus, when
        determining the file attributes, you must check
        if an attribute flag is set for target attributes.
    """
    ...


def SetAttribute(dir_item: EdsObject, file_attributes: int) -> int:
    """Changes attributes of files on a camera.

    :param EdsObject dir_item: The directory item.
    :param int file_attributes: Indicates the file attributes.
        As for the file attributes, OR values of the value
        defined by enum FileAttributes can be retrieved.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def CreateFileStream(
    filename: str, disposition: FileCreateDisposition, access: Access
) -> EdsObject:
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


def CreateMemoryStream(buffer_size: int) -> EdsObject:
    """Creates a stream in the memory of a host computer.
    In the case of writing in excess of the allocated buffer size,
        the memory is automatically extended.

    :param int buffer_size: The number of bytes of the memory to allocate.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The stream.
    """
    ...


def CreateMemoryStreamFromPointer(
    buffer: Union[bytes, bytearray, memoryview]
) -> EdsObject:
    """Creates a stream from the memory buffer you prepare.
    Unlike the buffer size of streams created by means of EdsCreateMemoryStream,
    the buffer size you prepare for streams created this way does not expand.

    :param Union[bytes, bytearray, memoryview] buffer: The buffer.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The stream.
    """
    ...


def GetPosition(stream_or_image: EdsObject) -> int:
    """Gets the current read or write position of the stream
        (that is, the file position indicator).

    :param EdsObject stream_or_image: The stream or image.
    :raises EdsError: Any of the sdk errors.
    :return int: The current stream pointer.
    """
    ...


def GetLength(stream_or_image: EdsObject) -> int:
    """Gets the stream size.

    :param EdsObject stream_or_image: The stream or image.
    :raises EdsError: Any of the sdk errors.
    :return int: The length of the stream.
    """
    ...


def CopyData(
    in_stream_or_image: EdsObject, write_size: int, out_stream_or_image: EdsObject
) -> None:
    """Copies data from the copy source stream to the copy destination stream.
    The read or write position of the data to copy is determined from
        the current file read or write position of the respective stream.
    After this API is executed, the read or write positions of the copy source
        and copy destination streams are moved an amount corresponding to
        inWriteSize in the positive direction.

    :param EdsObject in_stream_or_image: The input stream or image.
    :param int write_size: The number of bytes to copy.
    :param EdsObject out_stream_or_image: The output stream or image.
    """
    ...


def SetProgressCallback(
    camera: EdsObject, callback: Callable, option: ProgressOption
) -> None:
    """Register a progress callback function.
    An event is received as notification of progress during processing that
        takes a relatively long time, such as downloading files from a
        remote camera.
    If you register the callback function, the EDSDK calls the callback
        function during execution or on completion of the following APIs.
    This timing can be used in updating on-screen progress bars, for example.

    :param EdsObject stream_or_image: the stream or image object.
    :param Callable callback: The callback function.
        Expected signature (percent: int, cancel: bool) -> int.
    :param ProgressOption option: The option about progress is specified.
        Must be one of the following values.
            ProgressOption.Done
                When processing is completed,a callback function
                is called only once.
            ProgressOption.Periodically
                A callback function is performed periodically.
    :raises EdsError: Any of the sdk errors.
    """
    ...


def CreateImageRef(stream: EdsObject) -> EdsObject:
    """Creates an image object from an image file.
    Without modification, stream objects cannot be worked with as images.
    Thus, when extracting images from image files,
        you must use this API to create image objects.
    The image object created this way can be used to get image information
        (such as the height and width, number of color components, and
        resolution), thumbnail image data, and the image data itself.

    :param EdsObject stream: The stream.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The image.
    """
    ...


def GetImageInfo(image: EdsObject, image_source: ImageSource) -> Dict[str, Any]:
    """Gets image information from a designated image object.
    Here, image information means the image width and height,
        number of color components, resolution, and effective image area.

    :param EdsObject image: The image.
    :param ImageSource image_source: Of the various image data items in the image file,
        designate the type of image data representing the
        information you want to get. Designate the image as
        defined in Enum ImageSource.
            ImageSource.FullView
                The image itself (a full-sized image)
            ImageSource.Thumbnail
                A thumbnail image
            ImageSource.Preview
                A preview image
    :raises EdsError: Any of the sdk errors.
    :return Dict[str, Any]: Stores the image data information designated
        in inImageSource.
    """
    ...


def GetImage(
    image: EdsObject, image_source: ImageSource, image_type: TargetImageType,
    source_rect: Dict[str, Dict[str, int]], dest_size: Dict[str, int]
) -> EdsObject:
    """Gets designated image data from an image file, in the form of a
        designated rectangle.
    Returns uncompressed results for JPEGs and processed results
        in the designated pixel order (RGB, Top-down BGR, and so on) for
        RAW images.
    Additionally, by designating the input/output rectangle,
        it is possible to get reduced, enlarged, or partial images.
    However, because images corresponding to the designated output rectangle
        are always returned by the SDK, the SDK does not take the aspect
        ratio into account.
    To maintain the aspect ratio, you must keep the aspect ratio in mind
        when designating the rectangle.

    :param EdsObject image: The image for which to get the image data.
    :param ImageSource image_source: Designate the type of image data to get
        from the image file (thumbnail, preview, and so on).
    :param TargetImageType image_type: Designate the output image type. Because
        the output format of GetImage may only be RGB, only
        TargetImageType.RGB or TargetImageType.RGB16 can be designed.
        However, image types exceeding the resolution of
        image_source cannot be designated.
    :param Dict[str, Dict[str, int]] source_rect: Designate the coordinates
        and size of the rectangle to be retrieved from the source image.
    :param Dict[str, int] dest_size: Designate the rectangle size for output.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: the memory or file stream for output of the image.
    """
    ...


def CreateEvfImageRef(stream: EdsObject) -> EdsObject:
    """Creates an object used to get the live view image data set.

    :param EdsObject stream: The stream which opened to get EVF JPEG image.
    :raises EdsError: Any of the sdk errors.
    :return EdsObject: The EVFData.
    """
    ...


def DownloadEvfImage(camera: EdsObject, evf_image: EdsObject) -> None:
    """"Downloads the live view image data set for a camera currently in live view mode.
    Live view can be started by using the property ID:PropID.Evf_OutputDevice and
    data:OutputDevice.PC to call SetPropertyData.
    In addition to image data, information such as zoom, focus position, and histogram data
    is included in the image data set. Image data is saved in a stream maintained by EdsEvfImageRef.
    GetPropertyData can be used to get information such as the zoom, focus position, etc.
    Although the information of the zoom and focus position can be obtained from EvfImageRef,
    settings are applied to EdsCameraRef.

    :param EdsObject camera: The camera.
    :param EdsObject evf_image: The EVFData.
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


def SetPropertyEventHandler(
    camera: EdsObject, event: PropertyEvent, callback: Callable
) -> None:
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


def SetObjectEventHandler(
    camera: EdsObject, event: ObjectEvent, callback: Callable
) -> None:
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


def SetCameraStateEventHandler(
    camera: EdsObject, event: StateEvent, callback: Callable
) -> None:
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


def GetEvent() -> None:
    """This function acquires an event.
    In console application, please call this function regularly to acquire
        the event from a camera.
    :raises EdsError: Any of the sdk errors.
    """
    ...
