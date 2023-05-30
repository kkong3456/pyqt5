import pyautogui,time

print(pyautogui.size())

time.sleep(2)

print(pyautogui.position())

pyautogui.moveTo(100,200)
pyautogui.moveTo(100,200,2)

pyautogui.click()

pyautogui.click(button='right')

pyautogui.click(clicks=3,interval=1)