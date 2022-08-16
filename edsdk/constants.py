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


class PropID(IntEnum):
    # Camera Properties
    Unknown = 0x0000ffff

    ProductName = 0x00000002
    OwnerName = 0x00000004
    MakerName = 0x00000005
    DateTime = 0x00000006
    FirmwareVersion = 0x00000007
    BatteryLevel = 0x00000008
    SaveTo = 0x0000000b
    CurrentStorage = 0x0000000c
    CurrentFolder = 0x0000000d

    BatteryQuality = 0x00000010

    BodyIDEx = 0x00000015
    HDDirectoryStructure = 0x00000020

    TempStatus = 0x01000415

    # Image Properties
    ImageQuality = 0x00000100
    Orientation = 0x00000102
    ICCProfile = 0x00000103
    FocusInfo = 0x00000104
    WhiteBalance = 0x00000106
    ColorTemperature = 0x00000107
    WhiteBalanceShift = 0x00000108
    ColorSpace = 0x0000010d
    PictureStyle = 0x00000114
    PictureStyleDesc = 0x00000115
    PictureStyleCaption = 0x00000200

    # GPS Properties
    GPSVersionID = 0x00000800
    GPSLatitudeRef = 0x00000801
    GPSLatitude = 0x00000802
    GPSLongitudeRef = 0x00000803
    GPSLongitude = 0x00000804
    GPSAltitudeRef = 0x00000805
    GPSAltitude = 0x00000806
    GPSTimeStamp = 0x00000807
    GPSSatellites = 0x00000808
    GPSStatus = 0x00000809
    GPSMapDatum = 0x00000812
    GPSDateStamp = 0x0000081D

    # Capture Properties
    AEMode = 0x00000400
    DriveMode = 0x00000401
    ISOSpeed = 0x00000402
    MeteringMode = 0x00000403
    AFMode = 0x00000404
    Av = 0x00000405
    Tv = 0x00000406
    ExposureCompensation = 0x00000407
    FocalLength = 0x00000409
    AvailableShots = 0x0000040a
    Bracket = 0x0000040b
    WhiteBalanceBracket = 0x0000040c
    LensName = 0x0000040d
    AEBracket = 0x0000040e
    FEBracket = 0x0000040f
    ISOBracket = 0x00000410
    NoiseReduction = 0x00000411
    FlashOn = 0x00000412
    RedEye = 0x00000413
    FlashMode = 0x00000414
    LensStatus = 0x00000416
    Artist = 0x00000418
    Copyright = 0x00000419
    AEModeSelect = 0x00000436
    PowerZoom_Speed = 0x00000444

    # EVF Properties
    Evf_OutputDevice = 0x00000500
    Evf_Mode = 0x00000501
    Evf_WhiteBalance = 0x00000502
    Evf_ColorTemperature = 0x00000503
    Evf_DepthOfFieldPreview = 0x00000504

    # EVF Image Data Properties
    Evf_Zoom = 0x00000507
    Evf_ZoomPosition = 0x00000508
    Evf_Histogram = 0x0000050A
    Evf_ImagePosition = 0x0000050B
    Evf_HistogramStatus = 0x0000050C
    Evf_AFMode = 0x0000050E

    Record = 0x00000510

    Evf_HistogramY = 0x00000515
    Evf_HistogramR = 0x00000516
    Evf_HistogramG = 0x00000517
    Evf_HistogramB = 0x00000518

    Evf_CoordinateSystem = 0x00000540
    Evf_ZoomRect = 0x00000541
    Evf_ImageClipRect = 0x00000545

    Evf_PowerZoom_CurPosition = 0x00000550
    Evf_PowerZoom_MaxPosition = 0x00000551
    Evf_PowerZoom_MinPosition = 0x00000552

    # Limited Properties
    UTCTime = 0x01000016
    TimeZone = 0x01000017
    SummerTimeSetting = 0x01000018
    ManualWhiteBalanceData = 0x01000204
    MirrorLockUpState = 0x01000421
    FixedMovie = 0x01000422
    MovieParam = 0x01000423
    Aspect = 0x01000431
    MirrorUpSetting = 0x01000438
    AutoPowerOffSetting = 0x0100045e
    Evf_ClickWBCoeffs = 0x01000506
    EVF_RollingPitching = 0x01000544
    Evf_VisibleRect = 0x01000546
    StillMovieDivideSetting = 0x01000470
    CardExtension = 0x01000471
    MovieCardExtension = 0x01000472
    StillCurrentMedia = 0x01000473
    MovieCurrentMedia = 0x01000474
    FocusShiftSetting = 0x01000457
    MovieHFRSetting = 0x0100045d

    # DC Properties
    DC_Zoom = 0x00000600
    DC_Strobe = 0x00000601
    LensBarrelStatus = 0x00000605


class BatteryQuality(IntEnum):
    Low = 0
    Half = 1
    HI = 2
    Full = 3


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


class SaveTo(IntEnum):
    Camera = 1
    Host = 2
    Both = Camera | Host


class DeviceSubType(IntEnum):
    CanonPTPCamera = 1
    CanonPTP_IPCamera = 2


class CameraCommand(IntEnum):
    TakePicture = 0x00000000
    ExtendShutDownTimer = 0x00000001
    BulbStart = 0x00000002
    BulbEnd = 0x00000003
    DoEvfAf = 0x00000102
    DriveLensEvf = 0x00000103
    DoClickWBEvf = 0x00000104
    MovieSelectSwON = 0x00000107
    MovieSelectSwOFF = 0x00000108

    PressShutterButton = 0x00000004
    RequestRollPitchLevel = 0x00000109
    DrivePowerZoom = 0x0000010d
    SetRemoteShootingMode = 0x0000010f
    RequestSensorCleaning = 0x00000112


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


class ProgressOption(IntEnum):
    NoReport = 0
    Done = 1
    Periodically = 2


class CameraStatusCommand(IntEnum):
    UILock = 0x00000000
    UIUnLock = 0x00000001
    EnterDirectTransfer = 0x00000002
    ExitDirectTransfer = 0x00000003


class StorageType(IntEnum):
    Non = 0
    CF = 1
    SD = 2
    HD = 4
    CFast = 5
    CFe = 7


class FileAttributes(IntEnum):
    Normal = 0x00000000
    ReadOnly = 0x00000001
    Hidden = 0x00000002
    System = 0x00000004
    Archive = 0x00000020


class ImageSource(IntEnum):
    FullView = 0
    Thumbnail = 1
    Preview = 2
    RAWThumbnail = 3
    RAWFullView = 4
