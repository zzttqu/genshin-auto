import time
import cv2.cv2 as cv2
import numpy
import win32api, win32con, win32gui, win32ui
from PIL import Image

width = win32api.GetSystemMetrics(int(win32con.SM_CXVIRTUALSCREEN / 2))
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
# 创建设备描述表
total = 0
for _ in range(50):
    # 获取桌面
    t0 = time.time()
    hdesktop = win32gui.GetDesktopWindow()
    # 分辨率适应

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    # 创建一个内存设备描述表
    mem_dc = img_dc.CreateCompatibleDC()
    # 创建位图对象
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    # 截图至内存设备描述表
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)
    # 将截图保存到文件中
    bmpinfo = screenshot.GetInfo()
    bmpstr = screenshot.GetBitmapBits(True)
    # 内存释放
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
    # im_PIL = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

    im_opencv = numpy.frombuffer(bmpstr, dtype='uint8')
    im_opencv.shape = (height, width, 4)
    # cv2.cvtColor(im_opencv, cv2.COLOR_BGR2RGB)
    t1 = time.time()
    cv2.imshow('123', im_opencv)
    cv2.waitKey(0)
    total += int(t1 * 1000 - t0 * 1000)
print(total / 50)
