import pyautogui
# Consider screen as Cartesian co-ordinates where top left is (0,0) and Y-axis increses downwards and x axis on left
#we will try to automate mouse function 

print(pyautogui.size())
width ,height = pyautogui.size()
print(pyautogui.position())
pyautogui.moveTo(1700,200) #will move cursor to required position
pyautogui.moveTo(1700,700, duration=3) #will move  cursor as humans do in 3 seconds to required position
pyautogui.moveRel(50,0,duration=2.0) #will move right respect to current position
pyautogui.moveRel(0,-100,duration=2.0) #will move cursor upwards

pyautogui.click(48,46) #click at x=48 y=46
pyautogui.moveRel(0,50,duration=2.0)
pyautogui.click()#will directly click wherever  cursor is there
pyautogui.moveRel(0,50,duration=2.0)
pyautogui.doubleClick()#will click double

