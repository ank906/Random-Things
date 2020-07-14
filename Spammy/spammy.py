import time
import pyautogui

word = input("what am i spamming this time? : ")
count = 0
countmax = int(input("how many : "))
delay = int(input("how long is the delay (in seconds 0 by default)? : "))
time.sleep(1)
print("starting in : 3")
time.sleep(1)
print("starting in : 2")
time.sleep(1)
print("starting in : 1")

while(count != countmax):
    pyautogui.write(word)
    time.sleep(delay)
    pyautogui.press('enter')
    count += 1
