import pyautogui
import time

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
#opyautogui.moveTo(1510, 0, duration=0.5, tween=pyautogui.linear)
#pyautogui.moveTo(1465, 456, duration=0.6, tween=pyautogui.linear)
#pyautogui.doubleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
for _ in range(2):
    time.sleep(0.5)
    pyautogui.typewrite(message='dalao', interval=0.1)
    pyautogui.press('space')
    pyautogui.typewrite(message='tql', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('enter')
    #  pyautogui.press('alt')
    time.sleep(0.5)

# while True:
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(currentMouseX, currentMouseY)
#     time.sleep(0.5)
