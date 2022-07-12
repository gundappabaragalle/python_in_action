import pyautogui
def deleteline():
    pyautogui.keyDown("command")
    pyautogui.press('d')
    pyautogui.press('l')
    pyautogui.keyUp("command")

def remove_space():
    pyautogui.press('backspace')
    pyautogui.press('space')
    pyautogui.keyDown('command')
    pyautogui.press('return')
    pyautogui.keyUp('command')
    deleteline()
def delete_unwanted():
    for i in range(3):
        deleteline()