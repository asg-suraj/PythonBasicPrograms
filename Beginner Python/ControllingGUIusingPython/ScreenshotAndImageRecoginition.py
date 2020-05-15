import pyautogui
#if running in Linux install scrot by typing sudo apt-get install scrot
pyautogui.screenshot('C:\\Users\\win\\Desktop\\ss.png')

print(pyautogui.locateOnScreen('C:\\Users\\win\\Desktop\\sublimeLogo.png'))#will locate given image in our screen like logo or something so we need to input address of pic of logo to be find on screen
#will print location height and width of found
#pyautogui.locateCenterOnScreen('path') will find screen
