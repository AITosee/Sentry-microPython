from machine import I2C,UART
from  Sentry  import *
import time

sentry = Sentry2(log_level=LOG_ERROR)
#sentry.SetDebug(log_level=LOG_DEBUG)

#port = I2C(2, freq=400000)
port = UART(3)

err = sentry.begin(port)
print("sentry.begin: 0x%x"% err)
print("Sentry image_shape = %d %d"%(sentry.cols(), sentry.rows()))
 
err = sentry.VisionBegin(sentry_vision_e.kVisionLine)
print("sentry.VisionBegin(sentry_vision_e.kVisionLine):0x%x"% err)

tn = time.ticks_ms()
while True:
    ts = tn;
    obj_num = sentry.GetValue(sentry_vision_e.kVisionLine, kStatus)
    tn = time.ticks_ms()
    if obj_num:
        print("Totally %d objects in %dms:"%( obj_num, tn - ts))
        for i in range(obj_num):
            x = sentry.GetValue(sentry_vision_e.kVisionLine, kXValue)
            y = sentry.GetValue(sentry_vision_e.kVisionLine, kYValue)
            w = sentry.GetValue(sentry_vision_e.kVisionLine, kWidthValue)
            h = sentry.GetValue(sentry_vision_e.kVisionLine, kHeightValue)
            print("  obj: x=%d,y=%d,w=%d,h=%d"%( x, y, w, h))
