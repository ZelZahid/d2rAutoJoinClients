from time import sleep, time
import keyboard
import pyautogui

game_name = "zelly"
game_password = "123"
game_number = 0

def debug_mouse_position():
    while(True):
        x, y = pyautogui.position()
        print(f"Mouse position: (X: {x}, Y: {y})")
        sleep(0.2)

def on_press_f3():
    global game_number
    print("JOINING GAME:" , game_name,game_number)
    pyautogui.click(2900,90) #Join Game button
    sleep(0.2)
    pyautogui.click(2800,136) #Game Name Box
    sleep(0.01)
    #Delte all previous gamename text
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_name)  #writes gamename
    game_number_str = str(game_number)
    pyautogui.write(game_number_str)
    #game password:
    pyautogui.click(3000,136) #game pass box
    sleep(0.01)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_password)
    pyautogui.press('enter')    #enters game

    #Account 2:
    pyautogui.click(3550,384) #Join Game button
    sleep(0.2)
    pyautogui.click(3450,434) #Game Name Box
    sleep(0.01)
    #Delte all previous gamename text
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_name)  #writes gamename
    pyautogui.write(game_number_str)
    #game password:
    pyautogui.click(3600,434) #game pass box
    sleep(0.01)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_password)
    pyautogui.press('enter')    #enters game

    #game_number += 1
    #returns mouse to middle screen 960 505
    pyautogui.click(960,505)
    print("Done Joining")
def on_press_f4():
    global game_number
    print("NEW GAME!:" , game_name, game_number)
    #exiting Characters:
    pyautogui.press('esc')
    pyautogui.click(960,475)
    sleep(0.1)
    on_press_f5()

    #create New game
    game_number += 1
    pyautogui.click(1273,80)
    pyautogui.click(1450,175)
    #Delte all previous gamename text
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_name)  #writes gamename
    game_number_str = str(game_number)
    pyautogui.write(game_number_str)
    #game password:
    pyautogui.click(1430,245) #game pass box
    sleep(0.01)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(game_password)
    pyautogui.press('enter')    #enters game
    sleep(1.5)
    on_press_f3()
    pyautogui.press('alt')  #turns on item drop list on main


def on_press_f5():
    #2500,20    3400,320
    print("EXIT init()")
    pyautogui.click(2500,20)
    pyautogui.press('esc')
    pyautogui.click(2562,362)
    sleep(0.1)
    #exiting bot2
    pyautogui.click(3400,320)
    sleep(0.2)
    pyautogui.press('esc')
    pyautogui.click(3200,658)

    pyautogui.click(960,505) #Back to main screen
    print("Done Exiting Games")

#Main Loop:

#listen for F8 Debug Press
keyboard.add_hotkey('F8', debug_mouse_position)

#listen for 'F3' press
keyboard.add_hotkey('F3', on_press_f3)
#listen for 'F4' New Game Press
keyboard.add_hotkey('F4', on_press_f4)
#listen for 'F5' Exit press
keyboard.add_hotkey('F5', on_press_f5)

#keep program running to listen for the key press
keyboard.wait('F7')