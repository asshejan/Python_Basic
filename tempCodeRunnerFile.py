import pyautogui
import time

def pyramid(height):
   
    time.sleep(3)  
    for i in range(height):
        
        row = '#' * (i + 1)
        print(row)
        pyautogui.press('enter') 
       

    time.sleep(2)  


height = int(input())
pyramid(height)