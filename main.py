import pyautogui
import time
time.sleep(10)
f = open("beescript.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')