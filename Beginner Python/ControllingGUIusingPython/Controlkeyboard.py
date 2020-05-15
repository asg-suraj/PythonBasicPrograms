import pyautogui
#631 19
#378 66
pyautogui.click(631 ,19) #this positions may change so please check all positions using
#pyautogui.displayMousePosition() on cmd which gives location of cursor realtime..
pyautogui.click(378 ,66)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.typewrite('www.google.com') ; pyautogui.typewrite(['enter']) #here we can use ; in python hahaha
# it will use as enter button clicked pyautogui.press('enter') can also be used for same fashion
#for look more human like we can use 
#pyautogui.typewrite('www.google.com',interval=0.3)
#to press key in combination
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')

pyautogui.press('volumeup') #will press volume up key and can press keys defined in print(pyautogui.KEYBOARD_KEYS)



