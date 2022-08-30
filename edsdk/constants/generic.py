from enum import IntEnum


class DataType(IntEnum):
    Unknown = 0
    Bool = 1
    String = 2
    Int8 = 3
    UInt8 = 6
    Int16 = 4
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Float = 12
    Double = 13
    ByteBlock = 14
    Rational = 20
    Point = 21
    Rect = 22
    Time = 23

    Bool_Array = 30
    Int8_Array = 31
    Int16_Array = 32
    Int32_Array = 33
    UInt8_Array = 34
    UInt16_Array = 35
    UInt32_Array = 36
    Rational_Array = 37

    FocusInfo = 101
    PictureStyleDesc = 102


class CameraStatusCommand(IntEnum):
    UILock = 0x00000000
    UIUnLock = 0x00000001
    EnterDirectTransfer = 0x00000002
    ExitDirectTransfer = 0x00000003


class PropertyEvent(IntEnum):
    All = 0x00000100
    PropertyChanged = 0x00000101
    PropertyDescChanged = 0x00000102


class ObjectEvent(IntEnum):
    All = 0x00000200
    VolumeInfoChanged = 0x00000201
    VolumeUpdateItems = 0x00000202
    FolderUpdateItems = 0x00000203
    DirItemCreated = 0x00000204
    DirItemRemoved = 0x00000205
    DirItemInfoChanged = 0x00000206
    DirItemContentChanged = 0x00000207
    DirItemRequestTransfer = 0x00000208
    DirItemRequestTransferDT = 0x00000209
    DirItemCancelTransferDT = 0x0000020a
    VolumeAdded = 0x0000020c
    VolumeRemoved = 0x0000020d


class StateEvent(IntEnum):
    All = 0x00000300
    Shutdown = 0x00000301
    JobStatusChanged = 0x00000302
    WillSoonShutDown = 0x00000303
    ShutDownTimerUpdate = 0x00000304
    CaptureError = 0x00000305
    InternalError = 0x00000306
    AfResult = 0x00000309
    BulbExposureTime = 0x00000310
    PowerZoomInfoChanged = 0x00000311


class Access(IntEnum):
    Read = 0
    Write = 1
    ReadWrite = 2
    Error = 0xFFFFFFFF


class FileCreateDisposition(IntEnum):
    CreateNew = 0
    CreateAlways = 1
    OpenExisting = 2
    OpenAlways = 3
    TruncateExisting = 4


class ImageSource(IntEnum):
    FullView = 0
    Thumbnail = 1
    Preview = 2
    RAWThumbnail = 3
    RAWFullView = 4


class TargetImageType(IntEnum):
    Unknown = 0x00000000
    Jpeg = 0x00000001
    TIFF = 0x00000007
    TIFF16 = 0x00000008
    RGB = 0x00000009
    RGB16 = 0x0000000A
    DIB = 0x0000000B


class ProgressOption(IntEnum):
    NoReport = 0
    Done = 1
    Periodically = 2


class FileAttributes(IntEnum):
    Normal = 0x00000000
    ReadOnly = 0x00000001
    Hidden = 0x00000002
    System = 0x00000004
    Archive = 0x00000020


class ObjectFormat(IntEnum):
    Jpeg = 0x3801
    CR2 = 0xB103
    MP4 = 0xB982
    CR3 = 0xB108
    HEIF_CODE = 0xB10B


class StorageType(IntEnum):
    Non = 0
    CF = 1
    SD = 2
    HD = 4
    CFast = 5
    CFe = 7


class DeviceSubType(IntEnum):
    CanonPTPCamera = 1
    CanonPTP_IPCamera = 2


# What is this used for?
class BatteryLevel2(IntEnum):
    Empty = 0
    Low = 9
    Half = 49
    Normal = 80
    Hi = 69
    Quarter = 19
    Error = 0
    BCLevel = 0
    AC = 0xFFFFFFFF
    Unknown = 0xFFFFFFFE


# What is this used for?
class TransferOption(IntEnum):
    ByDirectTransfer = 1
    ByRelease = 2
    ToDesktop = 0x00000100


# What is this used for?
class StroboMode(IntEnum):
    Internal = 0
    ExternalETTL = 1
    ExternalATTL = 2
    ExternalTTL = 3
    ExternalAuto = 4
    ExternalManual = 5
    Manual = 6


# What is this used for?
class ETTL2Mode(IntEnum):
    Evaluative = 0
    Average = 1
