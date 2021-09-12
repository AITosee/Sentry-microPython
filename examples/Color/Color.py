from machine import I2C,UART
from  Sentry  import *
import time

sentry = Sentry(log_level=LOG_ERROR)
#sentry.SetDebug(log_level=LOG_DEBUG)

#port = I2C(2, freq=400000)
port = UART(3)

err = sentry.begin(port)
print("sentry.begin: 0x%x"% err)
print("Sentry image_shape = %d %d"%(sentry.cols(), sentry.rows()))

param_num = 4       # 1~25
sentry.SetParamNum(VisionColor, param_num)
  
for i in range(param_num):
    # Set x/y/w/h
    x_value = int(sentry.cols() * (i + 1) / (param_num + 1))
    y_value = int(120)
    width = int(i * 2 + 1)
    height = int(i * 2 + 1)
    print("SetParam[%d]: %d,%d,%d,%d"%( i, x_value, y_value, width, height))
    param = [x_value, y_value, width, height, 0]
    err = sentry.SetParam(VisionColor, param, i)
    if err:
        print("sentry.SetParam:0x%x\n"% err)
        while True:pass

    
err = sentry.VisionBegin(VisionColor)
print("sentry.VisionBegin(VisionColor):0x%x"% err)

obj_num = sentry.GetValue(VisionColor, Status)
print("obj_num:%d"% obj_num)

color = ('Black','White','Red','Yellow','Green','Purple','Blue')

tn = time.ticks_ms()
while True:
    ts = tn;
    obj_num = sentry.GetValue(VisionColor, Status)
    tn = time.ticks_ms()
    if obj_num:
        print("Totally %d objects in %dms:"%( obj_num, tn - ts))
        for i in range(obj_num):
            label = sentry.GetValue(VisionColor, Label, i)
            print("  obj[%d]: Label=%s"%(i,color[label-1]))
            

