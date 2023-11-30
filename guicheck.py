import pyautogui
import time

def pyramid(height):
   
    time.sleep(2)

    i = 1
    for i in range(height+1):
            
        pyautogui.write('#'*i)
        pyautogui.press('enter') 
       

    time.sleep(2)  


height = int(input())
pyramid(height)
