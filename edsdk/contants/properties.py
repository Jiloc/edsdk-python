from enum import IntEnum


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


# PropID.TimeZone
class TimeZone(IntEnum):
    None_ = 0x0000
    ChathamIslands = 0x0001
    Wellington = 0x0002
    SolomonIsland = 0x0003
    Syndney = 0x0004
    Adeladie = 0x0005
    Tokyo = 0x0006
    HongKong = 0x0007
    Bangkok = 0x0008
    Yangon = 0x0009
    Dacca = 0x000A
    Kathmandu = 0x000B
    Delhi = 0x000C
    Karachi = 0x000D
    Kabul = 0x000E
    Dubai = 0x000F
    Tehran = 0x0010
    Moscow = 0x0011
    Cairo = 0x0012
    Paris = 0x0013
    London = 0x0014
    Azores = 0x0015
    FernandoDeNoronha = 0x0016
    SaoPaulo = 0x0017
    Newfoundland = 0x0018
    Santiago = 0x0019
    Caracas = 0x001A
    NewYork = 0x001B
    Chicago = 0x001C
    Denver = 0x001D
    LosAngeles = 0x001E
    Anchorage = 0x001F
    Honolulu = 0x0020
    Samoa = 0x0021
    Riyadh = 0x0022
    Manaus = 0x0023
    UTC = 0x0100


# PropID.SummerTimeSetting
class SummerTimeSetting(IntEnum):
    Off = 0
    On = 1


# PropID.BatteryQuality
class BatteryQuality(IntEnum):
    Low = 0
    Half = 1
    HI = 2
    Full = 3


# PropID.SaveTo
class SaveTo(IntEnum):
    Camera = 1
    Host = 2
    Both = Camera | Host


# PropID.FocusInfo
class AFFrameValid(IntEnum):
    Invalid = 0
    Valid = 1


class AFFrameSelected(IntEnum):
    Unselected = 0
    Selected = 1


class AFFrameJustFocus(IntEnum):
    Standby = 0
    FocusingSuccess = 1
    FocusingFailure = 2
    ServoAFStopping = 3
    ServoAFRunning = 4


# PropID.ImageQuality
class ImageType(IntEnum):
    Unknown = 0x00000000
    Jpeg = 0x00000001
    CRW = 0x00000002
    RAW = 0x00000004
    CR2 = 0x00000006
    HEIF = 0x00000008


class ImageSize(IntEnum):
    Large = 0
    Middle = 1
    Small = 2
    Middle1 = 5
    Middle2 = 6
    Small1 = 14
    Small2 = 15
    Small3 = 16
    Unknown = 0xffffffff


class CompressQuality(IntEnum):
    Normal = 2
    Fine = 3
    Lossless = 4
    SuperFine = 5
    Unknown = 0xffffffff


class ImageQuality(IntEnum):
    # Jpeg Only
    LJ = 0x0010ff0f  # Jpeg Large
    MJ = 0x0110ff0f  # Jpeg Middle
    M1J = 0x0510ff0f  # Jpeg Middle1
    M2J = 0x0610ff0f  # Jpeg Middle2
    SJ = 0x0210ff0f  # Jpeg Small
    S1J = 0x0e10ff0f  # Jpeg Small1
    S2J = 0x0f10ff0f  # Jpeg Small2
    LJF = 0x0013ff0f  # Jpeg Large Fine
    LJN = 0x0012ff0f  # Jpeg Large Normal
    MJF = 0x0113ff0f  # Jpeg Middle Fine
    MJN = 0x0112ff0f  # Jpeg Middle Normal
    SJF = 0x0213ff0f  # Jpeg Small Fine
    SJN = 0x0212ff0f  # Jpeg Small Normal
    S1JF = 0x0E13ff0f  # Jpeg Small1 Fine
    S1JN = 0x0E12ff0f  # Jpeg Small1 Normal
    S2JF = 0x0F13ff0f  # Jpeg Small2
    S3JF = 0x1013ff0f  # Jpeg Small3

    # RAW + Jpeg
    LR = 0x0064ff0f  # RAW
    LRLJF = 0x00640013  # RAW + Jpeg Large Fine
    LRLJN = 0x00640012  # RAW + Jpeg Large Normal
    LRMJF = 0x00640113  # RAW + Jpeg Middle Fine
    LRMJN = 0x00640112  # RAW + Jpeg Middle Normal
    LRSJF = 0x00640213  # RAW + Jpeg Small Fine
    LRSJN = 0x00640212  # RAW + Jpeg Small Normal
    LRS1JF = 0x00640E13  # RAW + Jpeg Small1 Fine
    LRS1JN = 0x00640E12  # RAW + Jpeg Small1 Normal
    LRS2JF = 0x00640F13  # RAW + Jpeg Small2
    LRS3JF = 0x00641013  # RAW + Jpeg Small3

    LRLJ = 0x00640010  # RAW + Jpeg Large
    LRMJ = 0x00640110  # RAW + Jpeg Middle
    LRM1J = 0x00640510  # RAW + Jpeg Middle1
    LRM2J = 0x00640610  # RAW + Jpeg Middle2
    LRSJ = 0x00640210  # RAW + Jpeg Small
    LRS1J = 0x00640e10  # RAW + Jpeg Small1
    LRS2J = 0x00640f10  # RAW + Jpeg Small2

    # MRAW(SRAW1) + Jpeg
    MR = 0x0164ff0f  # MRAW(SRAW1)
    MRLJF = 0x01640013  # MRAW(SRAW1) + Jpeg Large Fine
    MRLJN = 0x01640012  # MRAW(SRAW1) + Jpeg Large Normal
    MRMJF = 0x01640113  # MRAW(SRAW1) + Jpeg Middle Fine
    MRMJN = 0x01640112  # MRAW(SRAW1) + Jpeg Middle Normal
    MRSJF = 0x01640213  # MRAW(SRAW1) + Jpeg Small Fine
    MRSJN = 0x01640212  # MRAW(SRAW1) + Jpeg Small Normal
    MRS1JF = 0x01640E13  # MRAW(SRAW1) + Jpeg Small1 Fine
    MRS1JN = 0x01640E12  # MRAW(SRAW1) + Jpeg Small1 Normal
    MRS2JF = 0x01640F13  # MRAW(SRAW1) + Jpeg Small2
    MRS3JF = 0x01641013  # MRAW(SRAW1) + Jpeg Small3

    MRLJ = 0x01640010  # MRAW(SRAW1) + Jpeg Large
    MRM1J = 0x01640510  # MRAW(SRAW1) + Jpeg Middle1
    MRM2J = 0x01640610  # MRAW(SRAW1) + Jpeg Middle2
    MRSJ = 0x01640210  # MRAW(SRAW1) + Jpeg Small

    # SRAW(SRAW2) + Jpeg
    SR = 0x0264ff0f  # SRAW(SRAW2)
    SRLJF = 0x02640013  # SRAW(SRAW2) + Jpeg Large Fine
    SRLJN = 0x02640012  # SRAW(SRAW2) + Jpeg Large Normal
    SRMJF = 0x02640113  # SRAW(SRAW2) + Jpeg Middle Fine
    SRMJN = 0x02640112  # SRAW(SRAW2) + Jpeg Middle Normal
    SRSJF = 0x02640213  # SRAW(SRAW2) + Jpeg Small Fine
    SRSJN = 0x02640212  # SRAW(SRAW2) + Jpeg Small Normal
    SRS1JF = 0x02640E13  # SRAW(SRAW2) + Jpeg Small1 Fine
    SRS1JN = 0x02640E12  # SRAW(SRAW2) + Jpeg Small1 Normal
    SRS2JF = 0x02640F13  # SRAW(SRAW2) + Jpeg Small2
    SRS3JF = 0x02641013  # SRAW(SRAW2) + Jpeg Small3

    SRLJ = 0x02640010  # SRAW(SRAW2) + Jpeg Large
    SRM1J = 0x02640510  # SRAW(SRAW2) + Jpeg Middle1
    SRM2J = 0x02640610  # SRAW(SRAW2) + Jpeg Middle2
    SRSJ = 0x02640210  # SRAW(SRAW2) + Jpeg Small

    # CRAW + Jpeg
    CR = 0x0063ff0f  # CRAW
    CRLJF = 0x00630013  # CRAW + Jpeg Large Fine
    CRMJF = 0x00630113  # CRAW + Jpeg Middle Fine
    CRM1JF = 0x00630513  # CRAW + Jpeg Middle1 Fine
    CRM2JF = 0x00630613  # CRAW + Jpeg Middle2 Fine
    CRSJF = 0x00630213  # CRAW + Jpeg Small Fine
    CRS1JF = 0x00630E13  # CRAW + Jpeg Small1 Fine
    CRS2JF = 0x00630F13  # CRAW + Jpeg Small2 Fine
    CRS3JF = 0x00631013  # CRAW + Jpeg Small3 Fine
    CRLJN = 0x00630012  # CRAW + Jpeg Large Normal
    CRMJN = 0x00630112  # CRAW + Jpeg Middle Normal
    CRM1JN = 0x00630512  # CRAW + Jpeg Middle1 Normal
    CRM2JN = 0x00630612  # CRAW + Jpeg Middle2 Normal
    CRSJN = 0x00630212  # CRAW + Jpeg Small Normal
    CRS1JN = 0x00630E12  # CRAW + Jpeg Small1 Normal

    CRLJ = 0x00630010  # CRAW + Jpeg Large
    CRMJ = 0x00630110  # CRAW + Jpeg Middle
    CRM1J = 0x00630510  # CRAW + Jpeg Middle1
    CRM2J = 0x00630610  # CRAW + Jpeg Middle2
    CRSJ = 0x00630210  # CRAW + Jpeg Small
    CRS1J = 0x00630e10  # CRAW + Jpeg Small1
    CRS2J = 0x00630f10  # CRAW + Jpeg Small2

    # HEIF
    HEIFL = 0x0080ff0f  # HEIF Large
    RHEIFL = 0x00640080  # RAW  + HEIF Large
    CRHEIFL =  0x00630080  # CRAW + HEIF Large

    HEIFLF = 0x0083ff0f  # HEIF Large Fine
    HEIFLN = 0x0082ff0f  # HEIF Large Normal
    HEIFMF = 0x0183ff0f  # HEIF Middle Fine
    HEIFMN = 0x0182ff0f  # HEIF Middle Normal
    HEIFS1F = 0x0e83ff0f  # HEIF Small1 Fine
    HEIFS1N = 0x0e82ff0f  # HEIF Small1 Normal
    HEIFS2F = 0x0f83ff0f  # HEIF Small2 Fine
    RHEIFLF = 0x00640083  # RAW + HEIF Large Fine
    RHEIFLN = 0x00640082  # RAW + HEIF Large Normal
    RHEIFMF = 0x00640183  # RAW + HEIF Middle Fine
    RHEIFMN = 0x00640182  # RAW + HEIF Middle Normal
    RHEIFS1F = 0x00640e83  # RAW + HEIF Small1 Fine
    RHEIFS1N = 0x00640e82  # RAW + HEIF Small1 Normal
    RHEIFS2F = 0x00640f83  # RAW + HEIF Small2 Fine
    CRHEIFLF = 0x00630083  # CRAW + HEIF Large Fine
    CRHEIFLN = 0x00630082  # CRAW + HEIF Large Normal
    CRHEIFMF = 0x00630183  # CRAW + HEIF Middle Fine
    CRHEIFMN = 0x00630182  # CRAW + HEIF Middle Normal
    CRHEIFS1F = 0x00630e83  # CRAW + HEIF Small1 Fine
    CRHEIFS1N = 0x00630e82  # CRAW + HEIF Small1 Normal
    CRHEIFS2F = 0x00630f83  # CRAW + HEIF Small2 Fine

    Unknown = 0xffffffff


# PropID.AEMode
class AEMode(IntEnum):
    Program = 0x00,
    Tv = 0x01
    Av = 0x02
    Manual = 0x03
    Bulb = 0x04
    A_DEP = 0x05
    DEP = 0x06
    Custom = 0x07
    Lock = 0x08
    Green = 0x09
    NightPortrait = 0x0A
    Sports = 0x0B
    Portrait = 0x0C
    Landscape = 0x0D
    Closeup = 0x0E
    FlashOff = 0x0F
    CreativeAuto = 0x13
    Movie = 0x14
    PhotoInMovie = 0x15
    SceneIntelligentAuto = 0x16
    SCN = 0x19
    NightScenes = 0x17
    BacklitScenes = 0x18
    Children = 0x1A
    Food = 0x1B
    CandlelightPortraits = 0x1C
    CreativeFilter = 0x1D
    RoughMonoChrome = 0x1E
    SoftFocus = 0x1F
    ToyCamera = 0x20
    Fisheye = 0x21
    WaterColor = 0x22
    Miniature = 0x23
    Hdr_Standard = 0x24
    Hdr_Vivid = 0x25
    Hdr_Bold = 0x26
    Hdr_Embossed = 0x27
    Movie_Fantasy = 0x28
    Movie_Old = 0x29
    Movie_Memory = 0x2A
    DirectMono= 0x2B
    Movie_Mini = 0x2C
    PanningAssist = 0x2D
    GroupPhoto = 0x2E
    Myself = 0x32
    PlusMovieAuto = 0x33
    SmoothSkin = 0x34
    Panorama = 0x35
    Silent = 0x36
    Flexible = 0x37
    OilPainting = 0x38
    Fireworks = 0x39
    StarPortrait = 0x3A
    StarNightscape = 0x3B
    StarTrails = 0x3C
    StarTimelapseMovie = 0x3D
    BackgroundBlur = 0x3E
    VideoBlog = 0x3F
    Unknown = 0xffffffff


# PropID.AEModeSelect
class AEModeSelect(IntEnum):
    Custom1 = 0x07
    Custom2 = 0x10
    Custom3 = 0x11
    SCNSpecialScene = 0x19


# PropID.DriveMode
class DriveMode(IntEnum):
    SingleShooting = 0x00000000
    ContinuousShooting = 0x00000001
    Video = 0x00000002
    HighSpeedContinuous = 0x00000004
    LowSpeedContinuous = 0x00000005
    SingleSilentShooting = 0x00000006
    SelfTimerContinuous = 0x00000007
    SelfTimer10Sec = 0x00000010
    SelfTimer2Sec = 0x00000011
    SuperHighSpeed14Fps = 0x00000012
    SilentSingleShooting = 0x00000013
    SilentContinuousShooting = 0x00000014
    SilentHighSpeedContinuous = 0x00000015
    SilentLowSpeedContinuous = 0x00000016


# PropID.ISOSpeed
class ISOSpeedCamera(IntEnum):
    ISOAuto = 0x00000000
    ISO6 = 0x00000028
    ISO12 = 0x00000030
    ISO25 = 0x00000038
    ISO50 = 0x00000040
    ISO100 = 0x00000048
    ISO125 = 0x0000004b
    ISO160 = 0x0000004d
    ISO200 = 0x00000050
    ISO250 = 0x00000053
    ISO320 = 0x00000055
    ISO400 = 0x00000058
    ISO500 = 0x0000005b
    ISO640 = 0x0000005d
    ISO800 = 0x00000060
    ISO1000 = 0x00000063
    ISO1250 = 0x00000065
    ISO1600 = 0x00000068
    ISO2000 = 0x0000006b
    ISO2500 = 0x0000006d
    ISO3200 = 0x00000070
    ISO4000 = 0x00000073
    ISO5000 = 0x00000075
    ISO6400 = 0x00000078
    ISO8000 = 0x0000007b
    ISO10000 = 0x0000007d
    ISO12800 = 0x00000080
    ISO16000 = 0x00000083
    ISO20000 = 0x00000085
    ISO25600 = 0x00000088
    ISO32000 = 0x0000008b
    ISO40000 = 0x0000008d
    ISO51200 = 0x00000090
    ISO64000 = 0x00000093
    ISO80000 = 0x00000095
    ISO102400 = 0x00000098
    ISO204800 = 0x000000a0
    ISO409600 = 0x000000a8
    ISO819200 = 0x000000b0
    NotValid_NoSettingsChanges = 0xffffffff


class ISOSpeedImage(IntEnum):
    ISO50 = 50
    ISO100 = 100
    ISO200 = 200
    ISO400 = 400
    ISO800 = 800
    ISO1600 = 1600
    ISO3200 = 3200
    ISO6400 = 6400
    ISO12800 = 12800
    ISO25600 = 25600
    ISO51200 = 51200
    ISO102400 = 102400


# PropID.MeteringMode
class MeteringMode(IntEnum):
    StopMetering = 1
    EvaluativeMetering = 3
    PartialMetering = 4
    CenterWeightedAveragingMetering = 5
    NotValid_NoSettingsChanges = 0xFFFFFFFF


# PropID.AFMode
class AFMode(IntEnum):
    OneShotAF = 0
    AIServoAF_ServoAF = 1
    AIFocusAF = 2
    ManualFocus = 3  # ReadOnly
    NotValid_NoSettingsChanges = 0xffffffff


# PropID.Av
Av = {
    0x08: "1", 0x0B: "1.1", 0x0C: "1.2", 0x0D: "1.2 (1/3)", 0x10: "1.4",
    0x13: "1.6", 0x14: "1.8", 0x15: "1.8 (1/3)", 0x18: "2", 0x1B: "2.2",
    0x1C: "2.5", 0x1D: "2.5 (1/3)", 0x20: "2.8", 0x23: "3.2", 0x85: "3.4",
    0x24: "3.5", 0x25: "3.5 (1/3)", 0x28: "4", 0x2B: "4.5", 0x2C: "4.5",
    0x2D: "5.0", 0x30: "5.6", 0x33: "6.3", 0x34: "6.7", 0x35: "7.1", 0x38: "8",
    0x3B: "9", 0x3C: "9.5", 0x3D: "10", 0x40: "11", 0x43: "13 (1/3)",
    0x44: "13", 0x45: "14", 0x48: "16", 0x4B: "18", 0x4C: "19", 0x4D: "20",
    0x50: "22", 0x53: "25", 0x54: "27", 0x55: "29", 0x58: "32", 0x5B: "36",
    0x5C: "38", 0x5D: "40", 0x60: "45", 0x63: "51", 0x64: "54", 0x65: "57",
    0x68: "64", 0x6B: "72", 0x6C: "76", 0x6D: "80", 0x70: "91",
    0xffffffff: "Not valid/no settings changes",
}


# PropID.Tv
Tv = {
    0x0C: "Bulb",
    0x10: "30\"", 0x13: "25\"", 0x14: "20\"", 0x15: "20\" (1/3)",
    0x18: "15\"", 0x1B: "13\"", 0x1C: "10\"", 0x1D: "10\" (1/3)",
    0x20: "8\"", 0x23: "6\" (1/3)", 0x24: "6\"", 0x25: "5\"", 0x28: "4\"",
    0x2B: "3\"2", 0x2C: "3", 0x2D: "2\"5", 0x30: "2", 0x33: "1\"6",
    0x34: "1\"5", 0x35: "1\"3", 0x38: "1", 0x3B: "0\"8", 0x3C: "0\"7",
    0x3D: "0\"6", 0x40: "0\"5", 0x43: "0\"4", 0x44: "0\"3", 0x45: "0\"3 (1/3)",
    0x48: "1/4", 0x4B: "1/5", 0x4C: "1/6", 0x4D: "1/6 (1/3)", 0x50: "1/8",
    0x53: "1/10 (1/3)", 0x54: "1/10", 0x55: "1/13", 0x58: "1/15",
    0x5B: "1/20 (1/3)", 0x5C: "1/20",  0x5D: "1/25", 0x60: "1/30",
    0x63: "1/40", 0x64: "1/45", 0x65: "1/50", 0x68: "1/60", 0x6B: "1/80",
    0x6C: "1/90", 0x6D: "1/100", 0x70: "1/125", 0x73: "1/160", 0x74: "1/180",
    0x75: "1/200", 0x78: "1/250", 0x7B: "1/320", 0x7C: "1/350", 0x7D: "1/400",
    0x80: "1/500", 0x83: "1/640", 0x84: "1/750", 0x85: "1/800", 0x88: "1/1000",
    0x8B: "1/1250", 0x8C: "1/1500", 0x8D: "1/1600", 0x90: "1/2000",
    0x93: "1/2500", 0x94: "1/3000", 0x95: "1/3200", 0x98: "1/4000",
    0x9B: "1/5000", 0x9C: "1/6000", 0x9D: "1/6400", 0xA0: "1/8000",
    0xA3: "1/10000", 0xA5: "1/12800", 0xA8: "1/16000",
    0xffffffff: "Not valid/no settings changes"
}


# PropID.ExposureCompensation
ExposureComponensation = {
    0x28: "+5",
    0x25: "+4 2/3",
    0x24: "+4 1/2",
    0x23: "+4 1/3",
    0x20: "+4",
    0x1D: "+3 2/3",
    0x1C: "+3 1/2",
    0x1B: "+3 1/3",
    0x18: "+3",
    0x15: "+2 2/3",
    0x14: "+2 1/2",
    0x13: "+2 1/3",
    0x10: "+2",
    0x0D: "+1 2/3",
    0x0C: "+1 1/2",
    0x0B: "+1 1/3",
    0x08: "+1",
    0x05: "+2/3",
    0x04: "+1/2",
    0x03: "+1/3",
    0x00: "0",
    0xFD: "-1/3",
    0xFC: "-1/2",
    0xFB: "-2/3",
    0xF8: "-1",
    0xF5: "-1 1/3",
    0xF4: "-1 1/2",
    0xF3: "-1 2/3",
    0xF0: "-2",
    0xED: "-2 1/3",
    0xEC: "-2 1/2",
    0xEB: "-2 2/3",
    0xE8: "-3",
    0xE5: "-3 1/3",
    0xE4: "-3 1/2",
    0xE3: "-3 2/3",
    0xE0: "-4",
    0xDD: "-4 1/3",
    0xDC: "-4 1/2",
    0xDB: "-4 2/3",
    0xD8: "-5",
    0xffffffff: "Not valid/no settings changes"
}


# PropID.Bracket
class Bracket(IntEnum):
    AEB = 0x01
    ISOB = 0x02
    WBB = 0x04
    FEB = 0x08
    Unknown = 0xffffffff


# PropID.WhiteBalanceBracket
class WhiteBalanceBracketMode(IntEnum):
    Off = 0
    ModeAB = 1
    ModeGM = 2
    NotSupported = 0xFFFFFFFF


# PropID.WhiteBalance
class WhiteBalance(IntEnum):
    Auto = 0
    Daylight = 1
    Cloudy = 2
    Tungsten = 3
    Fluorescent = 4
    Strobe = 5
    WhitePaper = 6
    Shade = 8
    ColorTemp = 9
    PCSet1 = 10
    PCSet2 = 11
    PCSet3 = 12
    WhitePaper2 = 15
    WhitePaper3 = 16
    WhitePaper4 = 18
    WhitePaper5 = 19
    PCSet4 = 20
    PCSet5 = 21
    AwbWhite = 23
    Click = -1
    Pasted = -2


# PropID.ColorSpace
class ColorSpace(IntEnum):
    sRGB = 1
    AdobeRGB = 2
    Unknown = 0xffffffff


# PropID.PictureStyle
class PictureStyle(IntEnum):
    Standard = 0x0081
    Portrait = 0x0082
    Landscape = 0x0083
    Neutral = 0x0084
    Faithful = 0x0085
    Monochrome = 0x0086
    Auto = 0x0087
    FineDetail = 0x0088
    User1 = 0x0021
    User2 = 0x0022
    User3 = 0x0023
    PC1 = 0x0041
    PC2 = 0x0042
    PC3 = 0x0043


# PropID.FlashOn
class FlashOn(IntEnum):
    NoFlash = 0
    Flash = 1


# PropID.FlashMode
class FlashModeType(IntEnum):
    None_ = 0
    Internal = 1
    ExternalETTL = 2
    ExternalATTL = 3
    InvalidValue = 0xFFFFFFFF


class FlashModeSynchroTiming(IntEnum):
    FirstCurtain = 0
    SecondCurtain = 1
    InvalidValue = 0xFFFFFFFF


# PropID.RedEye
class RedEye(IntEnum):
    Off = 0
    On = 1
    InvalidValue = 0xFFFFFFFF


# PropID.NoiseReduction
class NoiseReduction(IntEnum):
    Off = 0
    On1 = 1
    On2 = 2
    On = 3
    Auto = 4


# PropID.LensStatus
class LensStatus(IntEnum):
    NotAttached = 0
    Attached = 1


# PropID.DC_Strobe
class DcStrobe(IntEnum):
	Auto = 0
	On = 1
	Slowsynchro = 2
	Off = 3


# PropID.LensBarrelStatus
class DcLensBarrelState(IntEnum):
    Inner	= 0
    Outer	= 1


# PropID.Evf_OutputDevice
class EvfOutputDevice(IntEnum):
    TFT = 1
    PC = 2
    PC_Small = 8


# PropID.Evf_Mode
class EvfMode(IntEnum):
    Disable = 0
    Enable = 1


# PropID.Evf_DepthOfFieldPreview
class EvfDepthOfFieldPreview(IntEnum):
    OFF = 0x00000000
    ON = 0x00000001


# PropID.Evf_Zoom
class EvfZoom(IntEnum):
    Fit = 1
    x5 = 5
    x10 = 10


# PropID.Evf_HistogramStatus
class EvfHistogramStatus(IntEnum):
    Hide = 0
    Normal = 1
    Grayout = 2


# PropID.Evf_AFMode
class EvfAFMode(IntEnum):
    Quick = 0x00
    Live = 0x01
    LiveFace = 0x02
    LiveMulti = 0x03
    LiveZone = 0x04
    LiveSingleExpandCross = 0x05
    LiveSingleExpandSurround = 0x06
    LiveZoneLargeH = 0x07
    LiveZoneLargeV = 0x08
    LiveCatchAF = 0x09
    LiveSpotAF = 0x0a
    FlexibleZone1 = 0x0b
    FlexibleZone2 = 0x0c
    FlexibleZone3 = 0x0d
    WholeArea = 0x0e


# PropID.Record
class Record(IntEnum):
    EndMovieShooting = 0
    BeginMovieShooting = 4


# PropID.MirrorUpSetting
class MirrorUpSetting(IntEnum):
    Off = 0
    On = 1


# PropID.MirrorLockUpState
class MirrorLockUpState(IntEnum):
    Disable = 0
    Enable = 1
    DuringShooting = 2


# PropID.FixedMovie
class FixedMovie(IntEnum):
    MovideModeDisabled = 0x00
    MovieModeEnabled = 0x01


# PropID.MovieParam
MovieParam = {
    0x00000200: "1920x1080 23.98fps",
    0x00000210: "1920x1080 23.98fps For editing(ALL-I)",
    0x00000230: "1920x1080 23.98fps Standard(IPB)",
    0x00000300: "1920x1080 24.00fps",
    0x00000310: "1920x1080 24.00fps For editing(ALL-I)",
    0x00000330: "1920x1080 24.00fps Standard(IPB)",
    0x00000400: "1920x1080 25.00fps",
    0x00000410: "1920x1080 25.00fps For editing(ALL-I)",
    0x00000430: "1920x1080 25.00fps Standard(IPB)",
    0x00000500: "1920x1080 29.97fps",
    0x00000510: "1920x1080 29.97fps For editing(ALL-I)",
    0x00000530: "1920x1080 29.97fps Standard(IPB)",
    0x00000610: "1920x1080 50.00fps For editing(ALL-I)",
    0x00000630: "1920x1080 50.00fps Standard(IPB)",
    0x00000710: "1920x1080 59.94fps For editing(ALL-I)",
    0x00000730: "1920x1080 59.94fps Standard(IPB)",
    0x00001210: "1920x1080 23.98fps For editing(ALL-I)",
    0x00001230: "1920x1080 23.98fps Standard(IPB)",
    0x00001231: "1920x1080 23.98fps Light(IPB)",
    0x00001310: "1920x1080 24.00fps For editing(ALL-I)",
    0x00001330: "1920x1080 24.00fps Standard(IPB)",
    0x00001331: "1920x1080 24.00fps Light(IPB)",
    0x00001410: "1920x1080 25.00fps For editing(ALL-I)",
    0x00001430: "1920x1080 25.00fps Standard(IPB)",
    0x00001431: "1920x1080 25.00fps Light(IPB)",
    0x00001510: "1920x1080 29.97fps For editing(ALL-I)",
    0x00001530: "1920x1080 29.97fps Standard(IPB)",
    0x00001531: "1920x1080 29.97fps Light(IPB)",
    0x00001610: "1920x1080 50.00fps For editing(ALL-I)",
    0x00001630: "1920x1080 50.00fps Standard(IPB)",
    0x00001631: "1920x1080 50.00fps Light(IPB)",
    0x00001710: "1920x1080 59.94fps For editing(ALL-I)",
    0x00001730: "1920x1080 59.94fps Standard(IPB)",
    0x00001810: "1920x1080 100.0fps For editing(ALL-I)",
    0x00001731: "1920x1080 59.94fps Light(IPB)",
    0x00001910: "1920x1080 119.9fps For editing(ALL-I)",
    0x00010600: "1280x720 50.00fps",
    0x00010700: "1280x720 59.94fps",
    0x00010810: "1280x720 100.0fps For editing(ALL-I)",
    0x00010910: "1280x720 119.9fps For editing(ALL-I)",
    0x00011430: "1280x720 25.00fps Standard(IPB)",
    0x00011431: "1280x720 50.00fps Standard(IPB)",
    0x00011530: "1280x720 29.97fps Standard(IPB)",
    0x00011531: "1280x720 29.97fps Light(IPB)",
    0x00011610: "1280x720 50.00fps For editing(ALL-I)",
    0x00011630: "1280x720 50.00fps Standard(IPB)",
    0x00011710: "1280x720 59.94fps For editing(ALL-I)",
    0x00011730: "1280x720 59.94fps Standard(IPB)",
    0x00011810: "1280x720 100.0fps For editing(ALL-I)",
    0x00011830: "1280x720 100.0fps Standard(IPB)",
    0x00011910: "1280x720 119.9fps For editing(ALL-I)",
    0x00011930: "1280x720 119.9fps Standard(IPB)",
    0x00020400: "640x480 25.00fps",
    0x00020500: "640x480 29.97fps",
    0x00030240: "4096x2160 23.98fps Motion JPEG",
    0x00030340: "4096x2160 24.00fps Motion JPEG",
    0x00030440: "4096x2160 25.00fps Motion JPEG",
    0x00030540: "4096x2160 29.97fps Motion JPEG",
    0x00031210: "4096x2160 23.98fps For editing(ALL-I)",
    0x00031230: "4096x2160 23.98fps Standard(IPB)",
    0x00031231: "4096x2160 23.98fps Light(IPB)",
    0x00031310: "4096x2160 24.00fps For editing(ALL-I)",
    0x00031330: "4096x2160 24.00fps Standard(IPB)",
    0x00031331: "4096x2160 24.00fps Light(IPB)",
    0x00031410: "4096x2160 25.00fps For editing(ALL-I)",
    0x00031430: "4096x2160 25.00fps Standard(IPB)",
    0x00031431: "4096x2160 25.00fps Light(IPB)",
    0x00031510: "4096x2160 29.97fps For editing(ALL-I)",
    0x00031530: "4096x2160 29.97fps Standard(IPB)",
    0x00031531: "4096x2160 29.97fps Light(IPB)",
    0x00031610: "4096x2160 50.00fps For editing(ALL-I)",
    0x00031630: "4096x2160 50.00fps Standard(IPB)",
    0x00031631: "4096x2160 50.00fps Light(IPB)",
    0x00031710: "4096x2160 59.94fps For editing(ALL-I)",
    0x00031730: "4096x2160 59.94fps Standard(IPB)",
    0x00031731: "4096x2160 59.94fps Light(IPB)",
    0x00031810: "4096x2160 100.0fps For editing(ALL-I)",
    0x00031910: "4096x2160 119.9fps For editing(ALL-I)",
    0x00051210: "3840x2160 23.98fps For editing(ALL-I)",
    0x00051230: "3840x2160 23.98fps Standard(IPB)",
    0x00051231: "3840x2160 23.98fps Light(IPB)",
    0x00051310: "3840x2160 24.00fps For editing(ALL-I)",
    0x00051330: "3840x2160 24.00fps Standard(IPB)",
    0x00051331: "3840x2160 24.00fps Light (IPB)",
    0x00051410: "3840x2160 25.00fps For editing(ALL-I)",
    0x00051430: "3840x2160 25.00fps Standard(IPB)",
    0x00051431: "3840x2160 25.00fps Light(IPB)",
    0x00051510: "3840x2160 29.97fps For editing(ALL-I)",
    0x00051530: "3840x2160 29.97fps Standard(IPB)",
    0x00051531: "3840x2160 29.97fps Light(IPB)",
    0x00051610: "3840x2160 50.00fps For editing(ALL-I)",
    0x00051630: "3840x2160 50.00fps Standard(IPB)",
    0x00051631: "3840x2160 50.00fps Light(IPB)",
    0x00051710: "3840x2160 59.94fps For editing(ALL-I)",
    0x00051730: "3840x2160 59.94fps Standard(IPB)",
    0x00051731: "3840x2160 59.94fps Light(IPB)",
    0x00051810: "3840x2160 100.0fps For editing(ALL-I)",
    0x00051910: "3840x2160 119.9fps For editing(ALL-I)",
    0x00081210: "8192x4320 23.98fps For editing(ALL-I)",
    0x00081230: "8192x4320 23.98fps Standard(IPB)",
    0x00081231: "8192x4320 23.98fps Light(IPB)",
    0x00081310: "8192x4320 24.00fps For editing(ALL-I)",
    0x00081330: "8192x4320 24.00fps Standard(IPB)",
    0x00081331: "8192x4320 24.00fps Light(IPB)",
    0x00081410: "8192x4320 25.00fps For editing(ALL-I)",
    0x00081430: "8192x4320 25.00fps Standard(IPB)",
    0x00081431: "8192x4320 25.00fps Light(IPB)",
    0x00081510: "8192x4320 29.97fps For editing(ALL-I)",
    0x00081530: "8192x4320 29.97fps Standard(IPB)",
    0x00081531: "8192x4320 29.97fps Light(IPB)",
    0x00091210: "7680x4320 23.98fps For editing(ALL-I)",
    0x00091230: "7680x4320 23.98fps Standard(IPB)",
    0x00091231: "7680x4320 23.98fps Light(IPB)",
    0x00091330: "7680x4320 24.00fps Standard(IPB)",
    0x00091331: "7680x4320 24.00fps Light(IPB)",
    0x00091410: "7680x4320 25.00fps For editing(ALL-I)",
    0x00091430: "7680x4320 25.00fps Standard(IPB)",
    0x00091431: "7680x4320 25.00fps Light(IPB)",
    0x00091510: "7680x4320 29.97fps For editing(ALL-I)",
    0x00091530: "7680x4320 29.97fps Standard(IPB)",
    0x00091531: "7680x4320 29.97fps Light(IPB)",
    0x000a3270: "23.98fps (RAW)",
    0x000a3271: "23.98fps Light(RAW)",
    0x000a3370: "24.00fps (RAW)",
    0x000a3371: "24.00fps Light(RAW)",
    0x000a3470: "25.00fps (RAW)",
    0x000a3471: "25.00fps Light(RAW)",
    0x000a3570: "29.97fps (RAW)",
    0x000a3571: "29.97fps Light(RAW)",
    0x000a3670: "50.00fps (RAW)",
    0x000a3770: "59.94fps (RAW)",
    0x08001210: "1920x1080 23.98fps For editing(ALL-I)Crop",
    0x08001230: "1920x1080 23.98fps Standard(IPB)Crop",
    0x08001231: "1920x1080 23.98fps Light(IPB)Crop",
    0x08001410: "1920x1080 24.00fps For editing(ALL-I)Crop",
    0x08001430: "1920x1080 24.00fps Standard(IPB)Crop",
    0x08001431: "1920x1080 25.00fps For editing(ALL-I)Crop",
    0x08001510: "1920x1080 25.00fps Standard(IPB)Crop",
    0x08001530: "1920x1080 29.97fps For editing(ALL-I)Crop",
    0x08001531: "1920x1080 29.94fps Standard(IPB)Crop",
    0x08001610: "1920x1080 50.00fps For editing(ALL-I)Crop",
    0x08001630: "1920x1080 50.00fps Standard(IPB)Crop",
    0x08001631: "1920x1080 50.00fps Light(IPB)Crop",
    0x08001710: "1920x1080 59.94fps For editing(ALL-I)Crop",
    0x08001730: "1920x1080 59.94fps Standard(IPB)Crop",
    0x08001731: "1920x1080 59.94fps Light(IPB)Crop",
    0x08001810: "1920x1080 100.0fps For editing(ALL-I)Crop",
    0x08001910: "1920x1080 119.9fps For editing(ALL-I)Crop",
    0x08031210: "4096x2160 23.98fps For editing(ALL-I) Crop",
    0x08031230: "4096x2160 23.98fps Standard(IPB)Crop",
    0x08031231: "4096x2160 23.98fps Light(IPB)Crop",
    0x08031310: "4096x2160 24.00fps For editing(ALL-I)Crop",
    0x08031330: "4096x2160 24.00fps Standard(IPB)Crop",
    0x08031331: "4096x2160 24.00fps Light(IPB)Crop",
    0x08031410: "4096x2160 25.00fps For editing(ALL-I)Crop",
    0x08031430: "4096x2160 25.00fps Standard(IPB)Crop",
    0x08031431: "4096x2160 25.00fps Light(IPB)Crop",
    0x08031510: "4096x2160 29.97fps For editing(ALL-I)Crop",
    0x08031530: "4096x2160 29.94fps Standard(IPB)Crop",
    0x08031531: "4096x2160 29.94fps Light(IPB)Crop",
    0x08031610: "4096x2160 50.00fps For editing(ALL-I)Crop",
    0x08031630: "4096x2160 50.00fps Standard(IPB)Crop",
    0x08031631: "4096x2160 50.00fps Light(IPB)Crop",
    0x08031710: "4096x2160 59.94fps For editing(ALL-I)Crop",
    0x08031730: "4096x2160 59.94fps Standard(IPB)Crop",
    0x08031731: "4096x2160 59.94fps Light(IPB)Crop",
    0x08051210: "3840x2160 23.98fps For editing(ALL-I)",
    0x08051230: "3840x2160 23.98fps Standard(IPB)",
    0x08051231: "3840x2160 23.98fps Light(IPB)",
    0x08051410: "3840x2160 25.00fps For editing(ALL-I)",
    0x08051430: "3840x2160 25.00fps Standard(IPB)",
    0x08051431: "3840x2160 25.00fps Light (IPB)",
    0x08051510: "3840x2160 29.97fps For editing(ALL-I)",
    0x08051530: "3840x2160 29.97fps Standard(IPB)",
    0x08051531: "3840x2160 29.97fps Light(IPB)",
    0x08051610: "3840x2160 50.00fps For editing(ALL-I)",
    0x08051630: "3840x2160 50.00fps Standard(IPB)",
    0x08051631: "3840x2160 50.00fps Light (IPB)",
    0x08051710: "3840x2160 59.94fps For editing(ALL-I)",
    0x08051730: "3840x2160 59.94fps Standard(IPB)",
    0x08051731: "3840x2160 59.94fps Light (IPB)"
}


# PropID.TempStatus
class TempStatus1(IntEnum):
    Normal = 0x0000
    RestrictionMovieRecording = 0x0002


class TempStatus2(IntEnum):
    Normal = 0x0000
    WarningIndication = 0x0001
    ReduceFrameRate = 0x0002
    LiveViewProhibited = 0x0003
    ShootingProhibited = 0x0004
    DegratedStillImageQualityWarning = 0x0005


# PropID.Evf_RollingPitching
class EvfRollingPitchingStatus(IntEnum):
    StartingAngleInformationDisplay = 0x00
    StoppingAngleInformationDisplay = 0x01
    AngleInformationDetection = 0x02


class EvfRollingPitchingPosition(IntEnum):
    Horizontal = 0x00
    GripOnBottom = 0x01
    GripOnTop = 0x02
    UnableToDetect = 0x03
    PentaprismFacingDownward_UpsideDown = 0x04


# PropID.AutoPowerOffSetting
class AutoPowerOffSetting(IntEnum):
    Disabled = 0x00
    PowerOffNow = 0xffffffff  # shutdown camera


# PropID.Aspect
Aspect = {
    0x00000000: "Full-frame",
    0x00000001: "1:1 (aspect ratio)",
    0x00000002: "4:3 (aspect ratio)",
    0x00000007: "16:9 (aspect ratio)",
    0x0000000d: "1.6x (crop)",
}


# PropID.StillMovieDivideSetting
class StillMovieDivideSetting(IntEnum):
    Disabled = 0x00000000
    Enabled = 0x00000001


# PropID.CardExtension
class CardExtension(IntEnum):
    Standard = 0x00000000
    RecordToMultiple = 0x00000001
    RecordSeparately = 0x00000002
    AutoSwitchCard = 0x00000003


# PropID.MovieCardExtension
class MovieCardExtension(IntEnum):
    Standard = 0x00000000
    RecordToMultiple = 0x00000001
    Slow1Raw_Slot2MP4 = 0x00000002
    AutoSwitchCard = 0x00000003


# PropID.StillCurrentMedia
class StillCurrentMedia(IntEnum):
    Slot1 = 0x00000000
    Slot2 = 0x00000001


# PropID.MovieCurrentMedia
class MediaCurrentMedia(IntEnum):
    Slot1 = 0x00000000
    Slot2 = 0x00000001


# PropID.MovieHFRSetting
class MovieHFRSetting(IntEnum):
    Disabled = 0x00000000
    Enabled = 0x00000001


# PropID.AFEyeDetect
class AFEyeDetect(IntEnum):
    Disabled = 0x00000000
    Enabled = 0x00000001


# PropID.MovieServoAf
class MovieServoAf(IntEnum):
    Disabled = 0x00000000
    Enabled = 0x00000001
