import time
import pyautogui
from functions import delete_unwanted
from functions import remove_space
from functions import deleteline
total_blocks=int(input("total how may blocks are there in the text file: "))

time.sleep(5)
delete_unwanted()
pyautogui.press('down')
for x in range(total_blocks-1):
        delete_unwanted()
        remove_space()
deleteline()