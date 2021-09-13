from machine import I2C,UART
from  Sentry  import *
import time

sentry = Sentry()
#sentry.SetDebug(debug=True, level=LOG_DEBUG)

#port = I2C(2, freq=400000)
port = UART(3)

err = sentry.begin(port)
print("sentry.begin: 0x%x"% err)
print("Sentry image_shape = %d %d"%(sentry.cols(), sentry.rows()))
err = sentry.VisionBegin(kVisionQrCode)
print("sentry.VisionBegin(kkVisionQrCode):0x%x"% err)

tn = time.ticks_ms()


while True:
    ts = tn;
    obj_num = sentry.GetValue(kVisionQrCode, kStatus)
    tn = time.ticks_ms()
    if obj_num:
        print("Totally %d objects in %dms:"%( obj_num, tn - ts))
        x = sentry.GetValue(kVisionQrCode, kXValue)
        y = sentry.GetValue(kVisionQrCode, kYValue)
        w = sentry.GetValue(kVisionQrCode, kWidthValue)
        h = sentry.GetValue(kVisionQrCode, kHeightValue)
        c = sentry.GetQrCodeValue()
        print("  obj: x=%d,y=%d,w=%d,h=%d, value=%s"%( x, y, w, h, c))              
