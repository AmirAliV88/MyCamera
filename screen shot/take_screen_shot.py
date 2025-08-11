import pyautogui,time,random

print("after 3 sec will taking screenshot")
time.sleep(3)
pyautogui.screenshot(f"screenshot{random.randint(0, 100)}.png")


