import time
from Sentry import *
from mpython import *
from machine import UART


uart1 = UART(1, baudrate=57600, tx=Pin.P14, rx=Pin.P13)

sentry = Sentry2(0x60)

# 自定义函数
def UART():
  global my_variable, i, Start, angle, num
  # 定义掌控板与sentry2通讯所用的硬件串口引脚
  sentry.begin(uart1)
def I2C():
  global my_variable, i, Start, angle, num
  sentry.begin(i2c)
def Result_Display():
  global my_variable, i, Start, angle, num
  # Sentry2不主动返回检测识别结果，需要主控板发送指令进行读取。读取的流程：首先读取识别结果的数量，接收到指令后，Sentry2会刷新结果数据，如果结果数量不为零，那么主控再发送指令读取结果的相关信息。请务必按此流程构建程序。
  num = (sentry.GetValue(sentry2_vision_e.kVision20Classes, sentry_obj_info_e.kStatus))
  i = 1
  for index in range(num):
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kAirplane):
      oled.DispChar("AirPlane", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBicycle):
      oled.DispChar("Bicycle", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBird):
      oled.DispChar("Bird", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBoat):
      oled.DispChar("Boat", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBottle):
      oled.DispChar("Bottle", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kBus):
      oled.DispChar("Bus", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCar):
      oled.DispChar("Car", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCat):
      oled.DispChar("Cat", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kChair):
      oled.DispChar("Chair", 0, (2-1)*16, 1)
    if (sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)==class20_label_e.kCow):
      oled.DispChar("Cow", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 20):
      oled.DispChar("Tvmonitor", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 11):
      oled.DispChar("DiningTable", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 12):
      oled.DispChar("Dog", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 13):
      oled.DispChar("Horse", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 14):
      oled.DispChar("Motorbike", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 15):
      oled.DispChar("Person", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 16):
      oled.DispChar("PottedPlant", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 17):
      oled.DispChar("Sheep", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 18):
      oled.DispChar("Sofa", 0, (2-1)*16, 1)
    if ((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kLabel,i)) == 19):
      oled.DispChar("Train", 0, (2-1)*16, 1)
    oled.DispChar((str("x=") + str((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kXValue,i)))), 0, 32, 1)
    oled.DispChar((str("y=") + str((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kYValue,i)))), 64, 32, 1)
    oled.DispChar((str("w=") + str((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kWidthValue,i)))), 0, 48, 1)
    oled.DispChar((str("h=") + str((sentry.GetValue(sentry2_vision_e.kVision20Classes,sentry_obj_info_e.kHeightValue,i)))), 64, 48, 1)
    oled.show()
    time.sleep(0.2)
    oled.fill_rect(0, (2-1)*16, 128, 16, 0)
    oled.fill_rect(0, (3-1)*16, 128, 16, 0)
    oled.fill_rect(0, (4-1)*16, 128, 16, 0)
    oled.show()
    i = (i + 1)


num = 0
i = 0
# 等待sentry2初始化完毕，不可去掉。避免sentry2初始化未完成，主控板就发送指令
time.sleep(2)
I2C()
# 1、算法介绍
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#chapter-vision-20class-index
# 2、sentry2可以同时运行多个算法，但有限制要求，具体请查阅在线文档；
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#section-4
# 3、Sengo/Sentry系列产品参数与结果的编号都是从1开始；
# 4、正常使用时，应由主控器发送指令控制Sentry2算法的开启与关闭，而非通过摇杆手动进行操作；
# 5、如需Sentry2启动后，自行运行某种算法，可以在开启算法后，通过设置“寄存器”->“保存当前值”实现。
# 设置寄存器
# https://tosee.readthedocs.io/zh/latest/Sentry2/Hardware/index.html#section-3
sentry.VisionBegin(sentry2_vision_e.kVision20Classes)
oled.DispChar("Algo:20Class", 0, (1-1)*16, 1)
oled.show()
while True:
  Result_Display()