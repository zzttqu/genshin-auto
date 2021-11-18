import pyautogui
import time
from matchPicture import imgAutoClick

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
X, Y = imgAutoClick('QQ.png')
# X, Y = pyautogui.locateCenterOnScreen('QQ.png', grayscale=False)
print(X, Y)
pyautogui.moveTo(X, Y, duration=0.3, tween=pyautogui.linear)
pyautogui.click(x=None, y=None, interval=0, button='left')
time.sleep(1)
X, Y = imgAutoClick('fhy.png')
print(X, Y)
pyautogui.moveTo(X, Y, duration=0.3, tween=pyautogui.linear)
pyautogui.click(x=None, y=None, interval=0, button='left')
time.sleep(0.5)
pyautogui.doubleClick(x=X, y=Y, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)

# 这个是pyautogui的图片匹配，有一点不准
# X, Y = pyautogui.locateCenterOnScreen('fhy.png')
# 这一行是双击

for _ in range(2):
    time.sleep(0.5)
    pyautogui.typewrite(message='dalao', interval=0.1)
    pyautogui.press('space')
    pyautogui.typewrite(message='tql', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)

# while True:
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(currentMouseX, currentMouseY)
#     time.sleep(0.5)

