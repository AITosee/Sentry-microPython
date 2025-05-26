from machine import I2C,UART,Pin
from  Sentry  import *
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
 
# 1、Apriltag与二维码不同，请勿混淆。二者在使用时，周围一圈均需要留白；
# 2、算法介绍
# https://tosee.readthedocs.io/zh/latest/Sentry2/Vision/index.html#chapter-vision-apriltag-index
# 默认编码格式36H11，如需采用25H9与16H5格式的编码，请通过摇杆进行切换
# 3、参考视频
# https://www.bilibili.com/video/BV1dP4y1e7SW/?spm_id_from=333.1387.upload.video_card.click&vd_source=a6a4a13d17ed26ee248472534a8ec3cc
# https://www.bilibili.com/video/BV17r4y1d7G3/?spm_id_from=333.1387.upload.video_card.click&vd_source=a6a4a13d17ed26ee248472534a8ec3cc
# 4、如果需要更快的识别帧率，可以通过摇杆将识别模式更改为“快速”；
# 5、使用该算法时，可以配合调整zoom值、锐度、对比度、成像亮度来提升识别的的距离以及识别率。
# https://tosee.readthedocs.io/zh/latest/Sentry2/Hardware/index.html#section-21
# 6、正常使用时，应由主控器发送指令控制Sentry2算法的开启与关闭，而非通过摇杆手动进行操作；
# 7、满足特定限制条件下，Sentry2可以并行运行多个识别算法
# 参看“算法列表”
# https://tosee.readthedocs.io/zh/latest/Sentry2/Hardware/index.html#section-3
# 8、如需Sentry2启动后，自行运行某种算法，可以在开启算法后，通过设置“寄存器”->“保存当前值”实现。
# 参看“设置寄存器”
err = sentry.VisionBegin(sentry2_vision_e.kVisionAprilTag)
print("sentry.VisionBegin(sentry2_vision_e.kVisionAprilTag):0x%x"% err)


while True:
    # Sentry2不主动返回检测识别结果，需要主控板发送指令进行读取。读取的流程：首先读取识别结果的数量，接收到指令后，Sentry2会刷新结果数据，如果结果数量不为零，那么主控再发送指令读取结果的相关信息。请务必按此流程构建程序。
    obj_num = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kStatus)
    
    if obj_num:
        print("Totally %d tags: "%( obj_num ))
        for i in range(1,obj_num+1):
            x = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kXValue, i)
            y = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kYValue, i)
            w = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kWidthValue, i)
            h = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kHeightValue, i)
            l = sentry.GetValue(sentry2_vision_e.kVisionAprilTag, sentry_obj_info_e.kLabel, i)
            print("tag#%d: x=%d, y=%d, w=%d, h=%d, label=%d"%(i, x, y, w, h, l))
            time.sleep(0.2)
        print("\n")

            
            



