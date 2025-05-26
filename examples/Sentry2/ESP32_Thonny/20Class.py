from machine import I2C,UART,Pin
from Sentry import *
import time

# 等待Sentry2完成操作系统的初始化。此等待时间不可去掉，避免出现Sentry2尚未初始化完毕主控器已经开发发送指令的情况
time.sleep(2)

# 选择UART或者I2C通讯模式，Sentry2需要进行相应的设置，出厂默认为I2C模式
# 参看“设置通讯方式”
# https://tosee.readthedocs.io/zh/latest/Sentry2/Hardware/index.html#section-3
#########################################################################################################
# port = UART(2,rx=Pin(16),tx=Pin(17),baudrate=9600)
port = I2C(1,scl=Pin(22),sda=Pin(21),freq=400000)

# Sentry2默认通讯地址0x60，支持0x60-0x63四个地址。如果I2C总线挂接多个设备，请避免出现地址冲突
sentry = Sentry2(0x60)
 
err = sentry.begin(port)
print("sentry.begin: 0x%x"% err)
 
# 1、算法介绍
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#chapter-vision-20class-index
# 2、sentry2可以同时运行多个算法，但有限制要求，具体请查阅在线文档；
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#section-4
# 3、Sengo/Sentry系列产品参数与结果的编号都是从1开始；
# 4、正常使用时，应由主控器发送指令控制Sentry2算法的开启与关闭，而非通过摇杆手动进行操作；
# 5、满足特定限制条件下，Sentry2可以并行运行多个识别算法
# 参看“算法列表”
# https://tosee.readthedocs.io/zh/latest/Sentry2/Hardware/index.html#section-3
# 6、如需Sentry2启动后，自行运行某种算法，可以在开启算法后，通过设置“寄存器”->“保存当前值”实现。
# 参看“设置寄存器”
err = sentry.VisionBegin(sentry2_vision_e.kVision20Classes)
print("sentry.VisionBegin(sentry2_vision_e.kVision20Classes):0x%x"% err)

while True:
  # Sentry2不主动返回检测识别结果，需要主控板发送指令进行读取。读取的流程：首先读取识别结果的数量，接收到指令后，Sentry2会刷新结果数据，如果结果数量不为零，那么主控再发送指令读取结果的相关信息。请务必按此流程构建程序。
    obj_num = (sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kStatus))
    if obj_num:
        print("Totally %d objects: "%( obj_num ))
        for i in range(1,obj_num+1):
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kAirplane):
              print("object#%d: AirPlane, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBicycle):
              print("object#%d: Bicycle, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBird):
              print("object#%d: Bird, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBoat):
              print("object#%d: Boat, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBottle):
              print("object#%d: Bottle, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBus):
              print("object#%d: Bus, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCar):
              print("object#%d: Car, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCat):
              print("object#%d: Cat, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kChair):
              print("object#%d: Chair, "%(i), end='')
            if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCow):
              print("object#%d: Cow, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 11):
              print("object#%d: DiningTable, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 12):
              print("object#%d: Dog, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 13):
              print("object#%d: Horse, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 14):
              print("object#%d: Motorbike, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 15):
              print("object#%d: Person, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 16):
              print("object#%d: PottedPlant, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 17):
              print("object#%d: Sheep, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 18):
              print("object#%d: Sofa, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 19):
              print("object#%d: Train, "%(i), end='')
            if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 20):
              print("object#%d: Tvmonitor, "%(i), end='')
              
            x = sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kXValue, i)
            y = sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kYValue, i)
            w = sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kWidthValue, i)
            h = sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kHeightValue, i)
            print("x=%d, y=%d, w=%d, h=%d"%(x, y, w, h))
            time.sleep(0.2)
        print("\n")
