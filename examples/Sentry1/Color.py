from mpython import *
from Sentry import *

sentry1 = Sentry1(0x60)


sentry1.begin(i2c)
sentry1.VisionBegin(sentry1_vision_e.kVisionColor)
sentry1.LedSetColor(sentry_led_color_e.kLedWhite, sentry_led_color_e.kLedClose, 1)
sentry1.SetParamNum(sentry1_vision_e.kVisionColor, 1)
sentry1.SetParam(sentry1_vision_e.kVisionColor, [120, 120, 40, 40, 0], 1)
while True:
    count = sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {}".format(i, sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kRValue, i), sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kGValue, i), sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kBValue, i), sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kLabel, i)))
        if (sentry1.GetValue(sentry1_vision_e.kVisionColor, sentry_obj_info_e.kLabel, i) == color_label_e.kColorRed):
            print("red")
        i = i + 1
