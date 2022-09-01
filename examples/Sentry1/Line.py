from mpython import *
from Sentry import *

sentry1 = Sentry1(0x60)


sentry1.begin(i2c)
sentry1.VisionBegin(sentry1_vision_e.kVisionLine)
while True:
    count = sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {} {}".format(i, sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kXValue, i), sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kYValue, i), sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kWidthValue, i), sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kHeightValue, i), sentry1.GetValue(sentry1_vision_e.kVisionLine, sentry_obj_info_e.kLabel, i)))
        i = i + 1
