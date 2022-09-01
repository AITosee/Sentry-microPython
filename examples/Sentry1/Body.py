from mpython import *
from Sentry import *

sentry1 = Sentry1(0x60)


sentry1.begin(i2c)
sentry1.VisionBegin(sentry1_vision_e.kVisionBody)
sentry1.LedSetColor(sentry_led_color_e.kLedWhite, sentry_led_color_e.kLedClose, 1)
while True:
    count = sentry1.GetValue(sentry1_vision_e.kVisionBody, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {}".format(i, sentry1.GetValue(sentry1_vision_e.kVisionBody, sentry_obj_info_e.kXValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBody, sentry_obj_info_e.kYValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBody, sentry_obj_info_e.kWidthValue, i), sentry1.GetValue(sentry1_vision_e.kVisionBody, sentry_obj_info_e.kHeightValue, i)))
        i = i + 1
