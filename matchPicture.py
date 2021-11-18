import time

import cv2
import pyautogui
from PIL import ImageGrab
import numpy as np


def imgAutoClick(template, action=0):
    screen = ImageGrab.grab()
    template = cv2.imread(template, 0)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    w, h = template.shape[::-1]
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc  # 左上角的位置
    bottom_right = (top_left[0] + w, top_left[1] + h)  # 右下角的位置
    print(top+h/2, left+w/2)
    return top+h/3, left+w/3


# imgAutoClick(template='QQ.png')
# # 这部分是测试是否准确
# while True:
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(currentMouseX, currentMouseY)
#     time.sleep(0.5)
