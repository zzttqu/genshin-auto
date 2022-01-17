import time
import cv2.cv2 as cv2
import numpy
import win32api, win32con, win32gui, win32ui
from PIL import Image
import pyautogui

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)  # 每句所有的窗口，第一个参数是每枚举一个就会回调的函数

for h, t in hwnd_title.items():
    if t != "":
        print(h, t)
# hwnd = win32gui.FindWindow(None, '417等2个会话')
# win32gui.SetForegroundWindow(hwnd)

# 鼠标移动，第一个是X方向，第二个是Y方向
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 10, 10, 0, 0)
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, -200, 100, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, -200, 100, 0, 0)

# 获取桌面
hdesktop = win32gui.GetDesktopWindow()
# 分辨率适应
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
# 创建设备描述表
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
im_PIL = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

# 内存释放
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
im_opencv = numpy.frombuffer(bmpstr, dtype='uint8')
im_opencv.shape = (height, width, 4)
cv2.cvtColor(im_opencv, cv2.COLOR_BGR2RGB)
cv2.imshow('picture', im_opencv)

