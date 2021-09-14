import pyautogui
import pyperclip
import time

time.sleep(2)
pyautogui.alert("Não se mova!")
time.sleep(1.5)
pyautogui.click(175,740)
time.sleep(0.5)

angle = [0,45]
for l in range(230,700,25):
	if(True):
		#time.sleep(0.15)
		pyautogui.click(1195,l)
		pyautogui.hotkey("ctrl","t")
		#time.sleep(0.25)
		pyautogui.click(473,45)

		for b in range(0,5):
			pyautogui.keyDown("right")
			#time.sleep(0.05)
			pyautogui.keyUp("right")
			#time.sleep(0.05)

		for b in range(0,5):
			#time.sleep(0.05)
			pyautogui.press("backspace")

		#time.sleep(0.2)
		pyautogui.write(f"{angle[0]}".replace(".",","))
		#time.sleep(0.2)
		pyautogui.press("enter")
		#time.sleep(0.5)
		pyautogui.press("enter")
	angle[0] += 2.37
	print(angle[0])

pyautogui.alert("Tudo pronto!")


#Point(x=1195, y=644)
#Point(x=1226, y=230)