__version__ = "Sentry2 v0.0.1"
__author__ = "weiyanfengv@gmail.com"
__license__ = "http://unlicense.org"

import ustruct  # pylint: disable=import-error
from time import sleep_ms  # pylint: disable=no-name-in-module

SENTRY_DEVICE_ID = 0x04
SENTRY_FIRMWARE_VERSION = 0xFF

SENTRY_MAX_RESULT = 25

SENTRY_OK = 0x00
SENTRY_FAIL = 0x01
SENTRY_WRITE_TIMEOUT = 0x02
SENTRY_READ_TIMEOUT = 0x03
SENTRY_CHECK_ERROR = 0x04
SENTRY_UNSUPPORT_PARAM = 0x10
SENTRY_UNKNOWN_PROTOCOL = 0x11

# Protocol Error Type
SENTRY_PROTOC_OK = 0xE0
SENTRY_PROTOC_FAIL = 0xE1
SENTRY_PROTOC_UNKNOWN = 0xE2
SENTRY_PROTOC_TIMEOUT = 0xE3
SENTRY_PROTOC_CHECK_ERROR = 0xE4
SENTRY_PROTOC_LENGTH_ERROR = 0xE5
SENTRY_PROTOC_UNSUPPORT_COMMAND = 0xE6
SENTRY_PROTOC_UNSUPPORT_REG_ADDRESS = 0xE7
SENTRY_PROTOC_UNSUPPORT_REG_VALUE = 0xE8
SENTRY_PROTOC_READ_ONLY = 0xE9
SENTRY_PROTOC_RESTART_ERROR = 0xEA
SENTRY_PROTOC_RESULT_NOT_END = 0xEC

# Protocol
SENTRY_PROTOC_START = 0xFF
SENTRY_PROTOC_END = 0xED
SENTRY_PROTOC_COMMADN_SET = 0x01
SENTRY_PROTOC_COMMADN_GET = 0x02
SENTRY_PROTOC_SET_PARAM = 0x21
SENTRY_PROTOC_GET_RESULT = 0x23
SENTRY_PROTOC_MESSAGE = 0x11

# sentrys_vision
VisionColorRecog = 1
VisionColorDetect = 2
VisionAprilTag = 3
VisionLine = 4
VisionBody = 5
VisionCard = 6
VisionFace = 7
Vision20Classes = 8
VisionQrCode = 9
VisionObjTrack = 10
VisionMotionDetect = 11
VisionMaxType = 12

# sentry_led_color
LedClose = 0
LedRed = 1
LedGreen = 2
LedYellow = 3
LedBlue = 4
LedPurple = 5
LedCyan = 6
LedWhite = 7

# sentry_reg
RegDeviceId = 0x01
RegFirmwareVersion = 0x02
RegRestart = 0x03
RegSensorConfig1 = 0x04
RegLock = 0x05
RegLed1 = 0x06
RegLed2 = 0x07
RegLedLevel = 0x08
RegUart = 0x09
RegUSBCongig = 0x0B
RegHWConfig = 0x0F
RegCameraConfig1 = 0x10
RegCameraConfig2 = 0x11
RegCameraConfig3 = 0x12
RegCameraConfig4 = 0x13
RegCameraConfig5 = 0x14
RegFrameWidthH = 0x1B
RegFrameWidthL = 0x1C
RegFrameHeightH = 0x1D
RegFrameHeightL = 0x1E
RegFrameCount = 0x1F
RegVisionId = 0x20
RegVisionConfig1 = 0x21
RegVisionConfig2 = 0x22
RegParamNum = 0x23
RegParamId = 0x24
RegVisionStatus1 = 0x2A
RegVisionStatus2 = 0x2B
RegVisionDetect1 = 0x30
RegVisionDetect2 = 0x31
RegResultNumber = 0x34
RegResultId = 0x35
RegReadStatus1 = 0x36
RegParamValue1H = 0x70
RegParamValue1L = 0x71
RegParamValue2H = 0x72
RegParamValue2L = 0x73
RegParamValue3H = 0x74
RegParamValue3L = 0x75
RegParamValue4H = 0x76
RegParamValue4L = 0x77
RegParamValue5H = 0x78
RegParamValue5L = 0x79
RegResultData1H = 0x80
RegResultData1L = 0x81
RegResultData2H = 0x82
RegResultData2L = 0x83
RegResultData3H = 0x84
RegResultData3L = 0x85
RegResultData4H = 0x86
RegResultData4L = 0x87
RegResultData5H = 0x88
RegResultData5L = 0x89
RegSn = 0xD0


# sentry_led
Led1 = 0x00
Led2 = 0x01
LedAll = 0x02

# sentry_mode
SerialMode = 0x00
I2CMode = 0x01
UnknownMode = 0x02

# sentry_baudrate
Baud9600 = 0x00
Baud19200 = 0x01
Baud38400 = 0x02
Baud57600 = 0x03
Baud115200 = 0x04
Baud921600 = 0x05
Baud1152000 = 0x06
Baud2000000 = 0x07

# sentry_obj_info
Status = 1
XValue = 2
YValue = 3
WidthValue = 4
HeightValue = 5
Label = 6
RValue = 7
GValue = 8
BValue = 9

# sentry_camera_zoom
ZoomDefault = 0
Zoom1 = 1
Zoom2 = 2
Zoom3 = 3
Zoom4 = 4
Zoom5 = 5

# sentry_camera_fps
FPSNormal = 0
FPSHigh = 1

# sentry_camera_white_balance
AutoWhiteBalance = 0
LockWhiteBalance = 1
WhiteLight = 2
YellowLight = 3
WhiteBalanceCalibrating = 4


LOG_CRITICAL = 50
LOG_ERROR = 40
LOG_WARNING = 30
LOG_INFO = 20
LOG_DEBUG = 10
LOG_NOTSET = 0


class MuvisionLogger:

    _level = LOG_INFO
    _level_dict = {
        LOG_CRITICAL: "CRIT",
        LOG_ERROR: "ERROR",
        LOG_WARNING: "WARN",
        LOG_INFO: "INFO",
        LOG_DEBUG: "DEBUG",
    }

    def _level_str(self, level):
        l = self._level_dict.get(level)
        if l is not None:
            return l
        return "LVL%s" % level

    def setLevel(self, level):
        self._level = level

    def isEnabledFor(self, level):
        return level >= self._level

    def log(self, name, level, msg, *args):
        if self.isEnabledFor(level):
            levelname = self._level_str(level)
            msgformat = ["%s.%s:" % (name, levelname)]
            len_arg = len(args)

            if type(msg) == type("str") and len_arg > 0:
                len_msg = msg.count('%')
                if len_msg >= len_arg and len_msg > 0:
                    msgformat.append(msg % args)
                else:
                    msgformat.append(msg)
                    msgformat += args
            else:
                msgformat.append(msg)
                msgformat += args

            print(*msgformat, sep=" ")


class vision_result:
    result_data1 = 0
    result_data2 = 0
    result_data3 = 0
    result_data4 = 0
    result_data5 = 0
    bytestr = ""


class VisionState:
    def __init__(self, vision_type):
        self.vision_type = vision_type
        self.frame = 0
        self.detect = 0
        self.vision_result = []

        for _ in range(SENTRY_MAX_RESULT):
            self.vision_result.append(vision_result())


class SentryI2CMethod:
    """

    """

    def __init__(self, address, communication_port, logger=None):
        self.__mu_address = address
        self.__communication_port = communication_port
        self.__logger = logger

        if address not in communication_port.scan():
            raise ValueError(
                "SentryI2CMethod Init Error!!! address %#x cannot found!" % address)

    def Logger(self, *arg):  # level, format, args
        if self.__logger:
            self.__logger(self.__class__.__name__, *arg)

    def Set(self, reg_address, value):
        data = ustruct.pack("<b", value)
        self.__communication_port.writeto_mem(
            self.__mu_address, reg_address, data)

        self.Logger(LOG_DEBUG, "set-> reg:%#x var:%#x",
                    reg_address, value)

        return SENTRY_OK

    def Get(self, reg_address):
        data = ustruct.pack("<b", reg_address)
        self.__communication_port.writeto(self.__mu_address, data)

        value = self.__communication_port.readfrom(
            self.__mu_address, 1)
        if value:
            self.Logger(LOG_DEBUG, "Get-> reg:%#x var:%#x",
                        reg_address, value[0])
            return (SENTRY_OK, value[0])
        else:
            self.Logger(LOG_ERROR, "Get-> reg:%#x TimeOut!",
                        reg_address)

            return (SENTRY_READ_TIMEOUT, 0)

    def __get_result_data(self, RegResultDataL, RegResultDataH):
        err, result_data_tmp1 = self.Get(RegResultDataL)
        if err:
            return (err, 0)
        err, result_data_tmp2 = self.Get(RegResultDataH)
        if err:
            return (err, 0)

        return (err, result_data_tmp2 << 8 | result_data_tmp1)

    def Read(self, vision_type):
        vision_state = VisionState(vision_type)
        err = self.Set(RegVisionId, vision_type)
        if err:
            return (err, vision_state)

        err, vision_state.frame = self.Get(RegFrameCount)
        if err:
            return (err, vision_state)

        err, vision_state.detect = self.Get(RegResultNumber)
        if err:
            return (err, vision_state)

        if not vision_state.detect:
            return (SENTRY_OK, vision_state)

        vision_state.detect = SENTRY_MAX_RESULT if SENTRY_MAX_RESULT < vision_state.detect else vision_state.detect

        if VisionQrCode == vision_type:
            vision_state.detect = 1

        for i in range(vision_state.detect):
            err = self.Set(RegResultId, i+1)
            if err:
                return (err, vision_state)

            err, vision_state.vision_result[i].result_data1 = self.__get_result_data(
                RegResultData1L, RegResultData1H)
            if err:
                return (err, vision_state)
            err, vision_state.vision_result[i].result_data2 = self.__get_result_data(
                RegResultData2L, RegResultData2H)
            if err:
                return (err, vision_state)
            err, vision_state.vision_result[i].result_data3 = self.__get_result_data(
                RegResultData3L, RegResultData3H)
            if err:
                return (err, vision_state)
            err, vision_state.vision_result[i].result_data4 = self.__get_result_data(
                RegResultData4L, RegResultData4H)
            if err:
                return (err, vision_state)
            err, vision_state.vision_result[i].result_data5 = self.__get_result_data(
                RegResultData5L, RegResultData5H)
            if err:
                return (err, vision_state)

        return (SENTRY_OK, vision_state)

    def SetParam(self, vision_id, param, param_id):
        err = self.Set(RegVisionId, vision_id)
        if err:
            return err

        err = self.Set(RegParamId, param_id+1)
        if err:
            return err

        self.Set(RegParamValue1H, param[0])
        self.Set(RegParamValue1H, param[1])
        self.Set(RegParamValue2H, param[2])
        self.Set(RegParamValue2H, param[3])
        self.Set(RegParamValue3H, param[4])
        self.Set(RegParamValue3H, param[5])
        self.Set(RegParamValue4H, param[6])
        self.Set(RegParamValue4H, param[7])
        self.Set(RegParamValue5H, param[8])
        self.Set(RegParamValue5H, param[9])

        return SENTRY_OK

    def ReadQrCode(self):
        vision_state = self.Read(VisionQrCode)
        vision_state.vision_result[0].bytestr = ""

        for i in range(vision_state.vision_result[0].result_data5):
            result_id = i / 5 + 2
            offset = i % 5
            if 0 == i % 5:
                err = self.Set(RegVisionId, result_id)
                if err:
                    return err

            err, bytestr= chr(self.Get(RegResultData1L + 2 * offset))
            if err:
                return err
            vision_state.vision_result[0].bytestr +=bytestr
            
        return SENTRY_OK


class SentryUartMethod:
    """

    """

    def __init__(self, address, communication_port, logger=None):
        self.__mu_address = address
        self.__communication_port = communication_port
        self.__logger = logger
        # Setting serial port parameters
        self.__communication_port.init(timeout=1000, timeout_char=10)

    def Logger(self, *arg):  # level, format, args
        if self.__logger:
            self.__logger(self.__class__.__name__, *arg)

    def __cheak(self, data):
        count = 0
        for i in data[:-2]:
            count += i
        count &= 0xff

        if count == data[-2]:
            return SENTRY_PROTOC_OK
        else:
            return SENTRY_PROTOC_CHECK_ERROR

    def __protocol_read(self):

        count_ms = 0
        # The shortest receiving time of serial protocol is 6 bytes
        while self.__communication_port.any() < 6:
            count_ms += 1
            # The maximum waiting time for receiving data is 1s
            if count_ms < 1000:
                sleep_ms(1)
            else:
                return (SENTRY_PROTOC_TIMEOUT, [])

        self.Logger(LOG_DEBUG, "Waiting for reception takes %dms", count_ms)

        data_len = 0
        data_list = []
        for _ in range(self.__communication_port.any()):
            data_list.append(self.__communication_port.read(1)[0])
            if data_list[0] == SENTRY_PROTOC_START:
                data_list.append(self.__communication_port.read(1)[0])
                data_len = data_list[1]
                data_list += list(self.__communication_port.read(data_len-2))
                break

        if self.__logger:
            self.Logger(LOG_DEBUG, "Set rev-> %s",
                        ' '.join(['%02x' % b for b in data_list]))

        if data_len > 0 and data_len != len(data_list):
            return (SENTRY_PROTOC_CHECK_ERROR, [])

        if SENTRY_PROTOC_END != data_list[-1]:
            return (SENTRY_PROTOC_CHECK_ERROR, [])

        if self.__cheak(data_list) != SENTRY_PROTOC_OK:
            return (SENTRY_PROTOC_CHECK_ERROR, [])

        return (SENTRY_PROTOC_OK, tuple(data_list[3:]))

    def SetBuadrate(self, baud=Baud9600):
        baud_em = (Baud9600, Baud19200, Baud38400, Baud57600,
                   Baud115200, Baud921600, Baud1152000, Baud2000000)
        baud_se = (9600, 19200, 38400, 57600, 115200, 921600, 1152000, 2000000)
        if baud in baud_em:
            i = baud_em.index(baud)
            self.Logger(LOG_INFO, "SetBuadrate:%d", baud_se[i])
            self.__communication_port.init(baudrate=baud_se[i])

    def Set(self, reg_address, value):

        data_list = [SENTRY_PROTOC_START, 0, self.__mu_address,
                     SENTRY_PROTOC_COMMADN_SET, reg_address, value]
        data_list[1] = len(data_list)+2
        cheak_num = 0
        for da in data_list:
            cheak_num += da

        data_list.append(cheak_num & 0xff)
        data_list.append(SENTRY_PROTOC_END)

        data = ustruct.pack(">"+"b"*len(data_list), *tuple(data_list))

        if self.__logger:
            self.Logger(LOG_DEBUG, "Set req-> %s",
                        ' '.join(['%02x' % b for b in data]))

        if self.__communication_port.any():
            # Clear cache before sending
            self.__communication_port.read()
        self.__communication_port.write(data)

        try_time = 0
        while True:
            err, data = self.__protocol_read()
            if err == SENTRY_PROTOC_OK:
                if data[0] == SENTRY_PROTOC_OK or \
                        data[1] == SENTRY_PROTOC_COMMADN_GET or \
                        data[2] == reg_address:
                    return SENTRY_OK
                else:
                    return data[0]

            try_time += 1
            if try_time > 3:
                return SENTRY_READ_TIMEOUT

    def Get(self, reg_address):

        data_list = [SENTRY_PROTOC_START, 0, self.__mu_address,
                     SENTRY_PROTOC_COMMADN_GET, reg_address]
        data_list[1] = len(data_list)+2
        cheak_num = 0
        for da in data_list:
            cheak_num += da

        data_list.append(cheak_num & 0xff)
        data_list.append(SENTRY_PROTOC_END)

        data = ustruct.pack(">"+"b"*len(data_list), *tuple(data_list))

        if self.__logger:
            self.Logger(LOG_DEBUG, "Get req-> %s",
                        ' '.join(['%02x' % b for b in data]))

        if self.__communication_port.any():
            # Clear cache before sending
            self.__communication_port.read()
        self.__communication_port.write(data)

        try_time = 0
        while True:
            err, data = self.__protocol_read()
            if err == SENTRY_PROTOC_OK:
                if data[0] == SENTRY_PROTOC_OK or \
                        data[1] == SENTRY_PROTOC_COMMADN_GET:
                    return (SENTRY_OK, data[2])
                else:
                    return (data[0], 0)
            try_time += 1
            if try_time > 3:
                return (SENTRY_READ_TIMEOUT, 0)

    def Read(self, vision_type):
        vision_state = VisionState(vision_type)

        data_list = [SENTRY_PROTOC_START, 0, self.__mu_address,
                     SENTRY_PROTOC_GET_RESULT, vision_type, 0, 0]
        data_list[1] = len(data_list)+2
        cheak_num = 0
        for da in data_list:
            cheak_num += da

        data_list.append(cheak_num & 0xff)
        data_list.append(SENTRY_PROTOC_END)

        data = ustruct.pack(">"+"b"*len(data_list), *tuple(data_list))

        if self.__logger:
            self.Logger(LOG_DEBUG, "Read req-> %s",
                        ' '.join(['%02x' % b for b in data]))

        if self.__communication_port.any():
            # Clear cache before sending
            self.__communication_port.read()
        self.__communication_port.write(data)

        try_time = 0

        while True:
            err, data = self.__protocol_read()

            if self.__logger:
                self.Logger(LOG_DEBUG, "Read rev-> %s",
                            ' '.join(['%02x' % b for b in data]))

            if err == SENTRY_PROTOC_OK:
                if data[0] == SENTRY_PROTOC_OK or \
                        data[0] == SENTRY_PROTOC_RESULT_NOT_END or \
                        data[3] == vision_type:
                    if data[1] == SENTRY_PROTOC_GET_RESULT:
                        vision_state.frame = data[2]
                        vision_state.detect = 0
                        start_id = data[4]
                        stop_id = data[5]

                        if SENTRY_MAX_RESULT > stop_id:
                            return (SENTRY_UNSUPPORT_PARAM, None)

                        for i in range(start_id-1, stop_id):
                            j = vision_state.detect
                            vision_state.vision_result[i].result_data1 =\
                                data[10 * j + 6] << 8 | data[10 * j + 7]
                            vision_state.vision_result[i].result_data2 =\
                                data[10 * j + 8] << 8 | data[10 * j + 9]
                            vision_state.vision_result[i].result_data3 =\
                                data[10 * j + 10] << 8 | data[10 * j + 11]
                            vision_state.vision_result[i].result_data4 =\
                                data[10 * j + 12] << 8 | data[10 * j + 13]
                            vision_state.vision_result[i].result_data5 =\
                                data[10 * j + 14] << 8 | data[10 * j + 15]

                            vision_state.detect += 1

                        if data[0] == SENTRY_PROTOC_RESULT_NOT_END:
                            continue
                        else:
                            return (SENTRY_OK, vision_state)
                    else:
                        return (SENTRY_UNSUPPORT_PARAM, None)

            try_time += 1
            if try_time > 3:
                return (SENTRY_READ_TIMEOUT, None)

    def SetParam(self, vision_id, param: list, param_id):
        data_list = [SENTRY_PROTOC_START, 0, self.__mu_address,
                     SENTRY_PROTOC_COMMADN_SET, vision_id, param_id+1, param_id+1]

        data_list += param
        data_list[1] = len(data_list)+2
        cheak_num = 0
        for da in data_list:
            cheak_num += da

        data_list.append(cheak_num & 0xff)
        data_list.append(SENTRY_PROTOC_END)

        data = ustruct.pack(">"+"b"*len(data_list), *tuple(data_list))

        if self.__logger:
            self.Logger(LOG_DEBUG, "Set req-> %s",
                        ' '.join(['%02x' % b for b in data]))

        if self.__communication_port.any():
            # Clear cache before sending
            self.__communication_port.read()
        self.__communication_port.write(data)

        try_time = 0

        while True:
            err, data = self.__protocol_read()

            if self.__logger:
                self.Logger(LOG_DEBUG, "Set rev-> %s",
                            ' '.join(['%02x' % b for b in data]))

            if err == SENTRY_PROTOC_OK:
                if data[0] == SENTRY_PROTOC_OK:
                    if data[1] == SENTRY_PROTOC_SET_PARAM:
                        # FIXME: which is right?
                        # if (ret_val.buf[2] == vision_type:
                        return SENTRY_OK
                    # else:
                    #    return SENTRY_FAIL
                    else:
                        return SENTRY_UNSUPPORT_PARAM

            try_time += 1
            if try_time > 3:
                return SENTRY_READ_TIMEOUT

    def ReadQrCode(self):
        qrcode = VisionState(VisionQrCode)

        data_list = [SENTRY_PROTOC_START, 0, self.__mu_address,
                     SENTRY_PROTOC_GET_RESULT, VisionQrCode, 0, 0]

        data_list[1] = len(data_list)+2
        cheak_num = 0
        for da in data_list:
            cheak_num += da

        data_list.append(cheak_num & 0xff)
        data_list.append(SENTRY_PROTOC_END)

        data = ustruct.pack(">"+"b"*len(data_list), *tuple(data_list))

        if self.__logger:
            self.Logger(LOG_DEBUG, "Read req-> %s",
                        ' '.join(['%02x' % b for b in data]))

        if self.__communication_port.any():
            # Clear cache before sending
            self.__communication_port.read()
        self.__communication_port.write(data)

        try_time = 0

        while True:
            err, data = self.__protocol_read()

            if self.__logger:
                self.Logger(LOG_DEBUG, "Read rev-> %s",
                            ' '.join(['%02x' % b for b in data]))

            if err == SENTRY_PROTOC_OK:
                if data[0] == SENTRY_PROTOC_OK or data[3] == VisionQrCode:
                    if data[1] == SENTRY_PROTOC_GET_RESULT:
                        qrcode.frame = data[2]
                        qrcode.detect = 0
                        if data[5] == 0:
                            return SENTRY_OK
                        qrcode.detect = (data[5] - data[4] + 1) > 0
                        if not qrcode.detect:
                            return SENTRY_OK

                        qrcode.vision_result[0].result_data1 =\
                            data[10 + 6] << 8 | data[10 + 7]
                        qrcode.vision_result[0].result_data2 =\
                            data[10 + 8] << 8 | data[10 + 9]
                        qrcode.vision_result[0].result_data3 =\
                            data[10 + 10] << 8 | data[10 + 11]
                        qrcode.vision_result[0].result_data4 =\
                            data[10 + 12] << 8 | data[10 + 13]
                        qrcode.vision_result[0].result_data5 =\
                            data[10 + 14] << 8 | data[10 + 15]

                        for i in range(qrcode.vision_result[0].result_data5):
                            qrcode.vision_result[0].bytestr += chr(
                                data[17 + 2 * i])

                        return (SENTRY_OK, qrcode)
                    else:
                        return (SENTRY_UNSUPPORT_PARAM, None)

            try_time += 1
            if try_time > 3:
                return (SENTRY_READ_TIMEOUT, None)


class Sentry:
    """

    """

    def __init__(self, address=0x60, debug=False):
        self.__address = address
        self.__stream = None
        self.__img_w = 0
        self.__img_h = 0
        self.__vision_states = [None]*SENTRY_MAX_RESULT

        self.SetDebug(debug)

    @staticmethod
    def __setLevel(*arg):
        pass

    def Logger(self, *arg):  # level, format, args
        if self.__logger:
            self.__logger(self.__class__.__name__, *arg)

    def SetDebug(self, debug=False, level=LOG_INFO):
        if debug:
            self.__debug = MuvisionLogger()
            self.__logger = self.__debug.log
            self.SetLogLevel = self.__debug.setLevel
            self.SetLogLevel(level)
        else:
            self.__logger = None
            self.SetLogLevel = self.__setLevel

    def __SensorLockReg(self, lock: bool):
        return self.__stream.Set(RegLock, lock)

    def __SensorStartupCheck(self):
        err_count = 0
        while True:
            err_count += 1
            err, start_up = self.__stream.Get(RegSensorConfig1)
            if (not err) and start_up & 0x01:
                break

            sleep_ms(10)
            if err_count > 200:
                self.Logger(LOG_ERROR, "SensorStartupCheck error!")
                return SENTRY_UNKNOWN_PROTOCOL

    def __ProtocolVersionCheck(self):
        err_count = 0
        while True:
            err_count += 1
            err, protocol_version = self.__stream.Get(RegDeviceId)
            if (not err) and protocol_version == SENTRY_DEVICE_ID:
                break
            if err_count > 3:
                self.Logger(LOG_ERROR, "ProtocolVersionCheck error!")
                return SENTRY_UNKNOWN_PROTOCOL

        return err

    def GetImageShape(self):
        tmp = [0, 0]
        err, tmp[0] = self.__stream.Get(RegFrameWidthL)
        if err:
            return err
        err, tmp[1] = self.__stream.Get(RegFrameWidthH)
        if err:
            return err
        self.__img_w = tmp[1] << 8 | tmp[0]
        err, tmp[0] = self.__stream.Get(RegFrameHeightL)
        if err:
            return err
        err, tmp[1] = self.__stream.Get(RegFrameHeightH)
        if err:
            return err
        self.__img_h = tmp[1] << 8 | tmp[0]

        return SENTRY_OK

    def rows(self):
        return self.__img_h

    def cols(self):
        return self.__img_w

    def SensorInit(self):

        # Check sensor startup
        err = self.__SensorStartupCheck()
        if err:
            return err
        # Check sentry protocol version
        err = self.__ProtocolVersionCheck()
        if err:
            return err
        # Sensor set default if version is correction.
        err = self.SensorSetDefault()
        if err:
            return err
        # Get sensor image shape.
        err = self.GetImageShape()
        if err:
            return err

    def begin(self, communication_port=None):
        if "I2C" == communication_port.__class__.__name__:
            self.__stream = SentryI2CMethod(
                self.__address, communication_port, logger=self.__logger)
            self.Logger(LOG_INFO, "Begin I2C mode succeed!")

        elif 'UART' == communication_port.__class__.__name__:
            self.__stream = SentryUartMethod(
                self.__address, communication_port, logger=self.__logger)
            self.Logger(LOG_INFO, "Begin UART mode succeed!")

        elif communication_port == None:
            from machine import I2C, Pin  # pylint: disable=import-error
            communication_port = I2C(
                scl=Pin(Pin.P19), sda=Pin(Pin.P20), freq=400000)
            return self.begin(communication_port)

        else:
            return SENTRY_UNSUPPORT_PARAM

        if self.__stream:
            return self.SensorInit()

        return SENTRY_FAIL

    def VisionBegin(self, vision_type):
        err = self.VisionSetStatus(vision_type, True)
        if err:
            return err

        return SENTRY_OK

    def VisionEnd(self, vision_type):
        return self.VisionSetStatus(vision_type, False)

    def GetValue(self, vision_type, object_inf):
        '''
         Note: when getting the vision status, if the block is true, it will wait until the vision_type result is updated   
        '''
        if object_inf == Status:
            while True:
                if (self.UpdateResult(vision_type, True) & vision_type) != 0:
                    break
                else:
                    sleep_ms(10)  # pylint: disable=undefined-variable

            return self.__read(vision_type, object_inf)

    def SetParamNum(self, vision_type, max_num):
        err = self.__stream.Set(RegVisionId, vision_type)
        if err:
            return err

        err = self.__stream.Set(RegParamNum, max_num)

        return err

    def SetParam(self, vision_type, param, param_id):
        if param_id < 0 or param_id >= SENTRY_MAX_RESULT:
            return SENTRY_FAIL
        return self.__stream.SetParam(vision_type, param, param_id)

    def GetVisionState(self, vision_type):
        if vision_type >= VisionMaxType:
            return 0

        return self.__vision_states[vision_type-1]

    def VisionSetStatus(self, vision_type, enable: bool):

        err = self.__stream.Set(RegVisionId, vision_type)
        if err:
            return err

        err, vision_config_reg_value = self.__stream.Get(
            RegVisionConfig1)
        if err:
            return err

        status = vision_config_reg_value & 0x01
        if status != enable:
            vision_config_reg_value &= 0xfe
            vision_config_reg_value |= enable & 0x01

            err = self.__stream.Set(
                RegVisionConfig1, vision_config_reg_value)
            if err:
                return err

        if enable:
            self.__vision_states[vision_type-1] = VisionState(vision_type)

        else:
            self.__vision_states[vision_type-1] = None

    def VisionSetDefault(self, vision_type):

        err = self.__stream.Set(RegVisionId, vision_type)
        if err:
            return err
        err, vision_config_reg_value = self.__stream.Get(
            RegVisionConfig1)
        if err:
            return err

        vision_config_reg_value &= 0xfd
        vision_config_reg_value |= 0x01 << 1
        default_setting = (vision_config_reg_value >> 1) & 0x01
        err = self.__stream.Set(RegVisionConfig1,
                                vision_config_reg_value)
        if err:
            return err

        while default_setting:

            sleep_ms(10)

            err, vision_config_reg_value = self.__stream.Get(
                RegVisionConfig1)
            if err:
                return err
            default_setting = (vision_config_reg_value >> 1) & 0x01

        return SENTRY_OK

    def VisionGetStatus(self, vision_type):
        err = self.__stream.Set(RegVisionId, vision_type)
        if err:
            return 0

        err, vision_status1 = self.__stream.Get(
            RegVisionConfig1)

        if err:
            return 0

        return 0x01 & vision_status1

    def UpdateResult(self, vision_type):

        if vision_type >= VisionMaxType:
            return 0

        err, frame = self.__stream.Get(RegFrameCount)
        if err:
            return 0

        if frame == self.__vision_states[vision_type-1].frame:
            return 0

        while SENTRY_OK != self.__SensorLockReg(True):
            pass

        if vision_type == VisionQrCode:
            err, vision_state = self.__stream.ReadQrCode(vision_type)
        else:
            err, vision_state = self.__stream.Read(vision_type)

        while SENTRY_OK != self.__SensorLockReg(False):
            pass

        if err:
            return err

        self.__vision_states[vision_type-1] = vision_state

        return SENTRY_OK

    def __read(self, vision_type, object_inf, obj_id):

        if vision_type >= VisionMaxType:
            return 0

        obj_id = SENTRY_MAX_RESULT if obj_id > SENTRY_MAX_RESULT else obj_id

        vision_state = self.__vision_states[vision_type-1]
        if vision_state == None:
            return 0

        if object_inf == Status:
            return vision_state.detect
        elif object_inf == XValue:
            return vision_state.vision_result[obj_id].result_data1*100/self.__img_w
        elif object_inf == YValue:
            return vision_state.vision_result[obj_id].result_data2*100/self.__img_h
        elif object_inf == WidthValue:
            return vision_state.vision_result[obj_id].result_data3*100/self.__img_w
        elif object_inf == HeightValue:
            return vision_state.vision_result[obj_id].result_data4*100/self.__img_w
        elif object_inf == Label:
            return vision_state.vision_result[obj_id].result_data5
        elif object_inf == GValue:
            return vision_state.vision_result[obj_id].result_data1
        elif object_inf == RValue:
            return vision_state.vision_result[obj_id].result_data2
        elif object_inf == BValue:
            return vision_state.vision_result[obj_id].result_data3
        else:
            return 0

    def GetQrCodeValue(self):
        vision_state = self.__vision_states[VisionQrCode-1]
        if vision_state == None:
            return ""

        return vision_state.vision_result[0].bytestr

    def SensorSetRestart(self):
        err = self.__stream.Set(RegRestart, 1)
        if err:
            return err

        return SENTRY_OK

    def SensorSetDefault(self):
        err, sensor_config_reg_value = self.__stream.Get(RegSensorConfig1)
        if err:
            return err

        sensor_config_reg_value |= 0x08

        err = self.__stream.Set(RegSensorConfig1,
                                sensor_config_reg_value)
        while True:
            err, sensor_config_reg_value = self.__stream.Get(
                RegSensorConfig1)
            if err:
                return err

            if not (sensor_config_reg_value&0x08):
                self.Logger(LOG_INFO, "SensorSetDefault succeed!")
                break

        return err

    def LedSetMode(self, led, manual: bool, hold: bool):

        if Led1 == led:
            address = RegLed1

        elif Led2 == led:
            address = RegLed2

        elif LedAll == led:
            err = self.LedSetMode(Led1, manual, hold)
            if err:
                return err
            err = self.LedSetMode(Led2, manual, hold)
            return err

        else:
            return SENTRY_UNSUPPORT_PARAM

        err, led_reg_value = self.__stream.Get(address)
        if err:
            return err

        gmanual = led_reg_value & 0x01
        ghold = (led_reg_value >> 4) & 0x01

        if manual != gmanual or hold != ghold:
            led_reg_value &= 0xfe
            led_reg_value |= manual & 0x01

            led_reg_value &= 0xef
            led_reg_value |= (hold & 0x01) << 4

            err = self.__stream.Set(address, led_reg_value)
            if err:
                return err

        return SENTRY_OK

    def LedSetColor(self, led, detected_color, undetected_color, level):

        err, led_level = self.__stream.Get(RegLedLevel)
        if err:
            return err

        if Led1 == led:
            address = RegLed1
            led_level &= 0xF0
            led_level |= (level & 0x0F)
            self.__stream.Set(RegLedLevel, led_level)

        elif Led2 == led:
            address = RegLed2
            led_level &= 0x0F
            led_level |= (level << 4)
            self.__stream.Set(RegLedLevel, led_level)

        elif LedAll == led:
            err = self.LedSetColor(Led1, detected_color,
                                   undetected_color, level)
            if err:
                return err
            err = self.LedSetColor(Led2, detected_color,
                                   undetected_color, level)
            return err

        else:
            return SENTRY_UNSUPPORT_PARAM

        err, led_reg_value = self.__stream.Get(address)

        if err:
            return err

        led_reg_value &= 0xf1
        led_reg_value |= (detected_color & 0x07) << 1

        led_reg_value &= 0x1f
        led_reg_value |= (undetected_color & 0x07) << 5

        err = self.__stream.Set(address, led_reg_value)
        if err:
            return err

        return SENTRY_OK

    def CameraSetZoom(self, zoom):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            return err

        gzoom = camera_reg_value & 0x07

        if zoom != gzoom:
            camera_reg_value &= 0xf8
            camera_reg_value |= zoom & 0x07
            err = self.__stream.Set(
                RegCameraConfig1, camera_reg_value)
            if err:
                return err

        return err

    def CameraSetRotate(self, enable):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            return err

        rotate = (camera_reg_value >> 3) & 0x01
        if rotate != enable:
            camera_reg_value &= 0xf7
            camera_reg_value |= (enable & 0x01) << 3

            err = self.__stream.Set(
                RegCameraConfig1, camera_reg_value)
            if err:
                return err

        return err

    def CameraSetFPS(self, fps):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            return err

        gfps = (camera_reg_value >> 4) & 0x01
        if fps != gfps:
            camera_reg_value &= 0xef
            camera_reg_value |= (fps & 0x01) << 4
            err = self.__stream.Set(
                RegCameraConfig1, camera_reg_value)
            if err:
                return err

        return err

    def CameraSetAwb(self, awb):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            return err

        white_balance = (camera_reg_value >> 5) & 0x03

        if LockWhiteBalance == awb:
            camera_reg_value &= 0x1f
            camera_reg_value |= (awb & 0x03) << 5
            err = self.__stream.Set(
                RegCameraConfig1, camera_reg_value)
            if err:
                return err
            while (camera_reg_value >> 7) == 0:
                err, camera_reg_value = self.__stream.Get(
                    RegCameraConfig1)
                if err:
                    return err

        elif white_balance != awb:
            camera_reg_value &= 0x1f
            camera_reg_value |= (awb & 0x03) << 5
            err = self.__stream.Set(
                RegCameraConfig1, camera_reg_value)
            if err:
                return err

        return err

    def CameraGetZoom(self):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            pass

        return camera_reg_value & 0x07

    def CameraGetAwb(self):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            pass

        return (camera_reg_value >> 5) & 0x03

    def CameraGetRotate(self):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            pass

        return (camera_reg_value >> 3) & 0x01

    def CameraGetFPS(self):

        err, camera_reg_value = self.__stream.Get(
            RegCameraConfig1)
        if err:
            pass

        return (camera_reg_value >> 4) & 0x01

    def UartSetBaudrate(self, baud):
        err, uart_reg_value = self.__stream.Get(RegUart)
        baudrate = uart_reg_value & 0x07
        if (not err) and baudrate != baud:
            uart_reg_value &= 0xf8
            uart_reg_value |= baud & 0x07
            err = self.__stream.Set(RegUart, uart_reg_value)
        if not err:
            if 'SentryUartMethod' == self.__stream.__class__.__name__:
                self.__stream.SetBuadrate(baud)
                sleep_ms(500)

        return err
