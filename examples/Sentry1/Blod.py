from mpython import *
from Sentry import *

sentry1 = Sentry1(0x60)


sentry1.begin(i2c)
sentry1.VisionBegin(sentry1_vision_e.kVisionBlob)
sentry1.LedSetColor(sentry_led_color_e.kLedWhite, sentry_led_color_e.kLedClose, 1)
sentry1.SetParamNum(sentry1_vision_e.kVisionBlob, 1)
sentry1.SetParam(sentry1_vision_e.kVisionBlob, [0, 0, 15, 15, color_label_e.kColorWhite], 1)
while True:
    count = sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {} {}".format(i, sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kXValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kYValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kWidthValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kHeightValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBlob, sentry_obj_info_e.kLabel, i)))
        i = i + 1
