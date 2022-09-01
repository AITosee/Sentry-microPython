from mpython import *
from Sentry import *

sentry = Sentry2(0x61)


sentry.begin(i2c)
sentry.VisionBegin(sentry2_vision_e.kVisionLine)
while True:
    count = sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kStatus)
    i = 1
    for count in range(int(count)):
        print("{} {} {} {} {} {}".format(i, sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kXValue, i), sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kYValue, i), sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kWidthValue, i), sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kHeightValue, i), sentry.GetValue(sentry2_vision_e.kVisionLine, sentry_obj_info_e.kLabel, i)))
        i = i + 1
