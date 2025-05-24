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
 
err = sentry.kVisionBegin(sentry2_vision_e.kVisionAprilTag)
print("sentry.VisionBegin(sentry2_vision_e.kVisionAprilTag):0x%x"% err)

tn = time.ticks_ms()
while True:
    ts = tn
    obj_num = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kStatus)
    tn = time.ticks_ms()
    if obj_num:
        print("Totally %d objects in %dms:"%( obj_num, tn - ts))
        for i in range(1,obj_num+1):
            x = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kXValue, i)
            y = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kYValue, i)
            w = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kWidthValue, i)
            h = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kHeightValue, i)
            l = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kLabel, i)
            print("  obj: x=%d,y=%d,w=%d,h=%d, Label=%d"%( x, y, w, h, l))

            
            



