import time

import numpy
import pyautogui
from cv2 import cv2
from PIL import Image

total = 0
t0 = time.time()
for i in range(10):
    img = pyautogui.screenshot(region=[0, 0, 1920, 1080])  # x,y,w,h
    img.save('1.jpg', quality=95)
t1 = time.time()
print(int(t1 * 1000 - t0 * 1000) / 10)
