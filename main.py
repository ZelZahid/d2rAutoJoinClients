from time import sleep, time
import keyboard
import pyautogui

game_name = "zt"   #2,972,000,000
game_password = "1"
game_number = 1     #zt-38
numOfAccounts = 7       #3,5,7,8

def debug_mouse_position():
    while(True):
        x, y = pyautogui.position()
        print(f"Mouse position: (X: {x}, Y: {y})")
        sleep(0.2)

#join gameg
def on_press_f3():
    global game_number
    print("JOINING GAME:" , game_name,game_number)
    pyautogui.click(2200,20)
    pyautogui.click(2900,90) #Join Game button
    sleep(0.05)
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
    pyautogui.click(3500,925)
    pyautogui.click(3550,384) #Join Game button
    sleep(0.05)
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

    if(numOfAccounts >= 5):
            #Account 3:
        pyautogui.click(3500,20)
        pyautogui.click(3553,90) #Join Game button
        sleep(0.05)
        pyautogui.click(3450,136) #Game Name Box
        sleep(0.01)
        #Delte all previous gamename text
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(game_name)  #writes gamename
        pyautogui.write(game_number_str)
        #game password:
        pyautogui.click(3650,136) #game pass box
        sleep(0.01)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(game_password)
        pyautogui.press('enter')    #enters game

        #Account 4:
        pyautogui.click(2000,1020)
        pyautogui.click(2880,390) #Join Game button
        sleep(0.05)
        pyautogui.click(2880,434) #Game Name Box
        sleep(0.01)
        #Delte all previous gamename text
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(game_name)  #writes gamename
        pyautogui.write(game_number_str)
        #game password:
        pyautogui.click(3000,434) #game pass box
        sleep(0.01)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(game_password)
        pyautogui.press('enter')    #enters game

        if(numOfAccounts >= 7):
            #Account 5:
            pyautogui.click(-1874,1000)
            pyautogui.click(-965,382) #Join Game button
            sleep(0.05)
            pyautogui.click(-965,431) #Game Name Box
            sleep(0.01)
            #Delte all previous gamename text
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(game_name)  #writes gamename
            pyautogui.write(game_number_str)
            #game password:
            pyautogui.click(-871,434) #game pass box
            sleep(0.01)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(game_password)
            pyautogui.press('enter')    #enters game

            #Account 6:
            pyautogui.click(-1700,15)
            pyautogui.click(-970,85) #Join Game button
            sleep(0.05)
            pyautogui.click(-970,136) #Game Name Box
            sleep(0.01)
            #Delte all previous gamename text
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(game_name)  #writes gamename
            pyautogui.write(game_number_str)
            #game password:
            pyautogui.click(-857,136) #game pass box
            sleep(0.01)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(game_password)
            pyautogui.press('enter')    #enters game

            if(numOfAccounts == 8):
                #Account 7:
                pyautogui.click(-50,1050)
                pyautogui.click(-295,385) #Join Game button
                sleep(0.05)
                pyautogui.click(-392,434) #Game Name Box
                sleep(0.01)
                #Delte all previous gamename text
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                pyautogui.write(game_name)  #writes gamename
                pyautogui.write(game_number_str)
                #game password:
                pyautogui.click(-200,434) #game pass box
                sleep(0.01)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                pyautogui.write(game_password)
                pyautogui.press('enter')    #enters game

    #game_number += 1
    #returns mouse to middle screen 960 505
    pyautogui.click(-350,20)
    pyautogui.click(2200,20)#click bo Buff Bot
    pyautogui.click(960,505)
    print("Done Joining")
    sleep(0.05)
#next game
def on_press_f4():
    global game_number
    print("NEW GAME!:" , game_name, game_number)
    #exiting Characters:
    pyautogui.press('esc')
    pyautogui.click(960,475)
    sleep(0.01)
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
    sleep(0.01)
    on_press_f3()
    sleep(0.01)
    pyautogui.press('alt')  #turns on item drop list on main

#exit game
def on_press_f5():
    #2500,20    3400,320
    print("EXIT init()")
    pyautogui.click(2200,20)
    pyautogui.press('esc')
    pyautogui.click(2562,362)
    sleep(0.01)
    #exiting bot2
    pyautogui.click(3500,925)
    sleep(0.01)
    pyautogui.press('esc')
    pyautogui.click(3200,658)
    if(numOfAccounts >= 5):
        #exiting bot3
        pyautogui.click(3500,20)
        sleep(0.01)
        pyautogui.press('esc')
        pyautogui.click(3200,360)
        #exiting bot4
        pyautogui.click(2000,1020)
        sleep(0.01)
        pyautogui.press('esc')
        pyautogui.click(2560,664)
        if(numOfAccounts >= 7):
            #exiting bot5
            pyautogui.click(-1874,1000)
            sleep(0.01)
            pyautogui.press('esc')
            pyautogui.click(-1284,660)
            #exiting bot6
            pyautogui.click(-1700,15)
            sleep(0.01)
            pyautogui.press('esc')
            pyautogui.click(-1284,360)

            if(numOfAccounts == 8):
                #exit bot 7
                pyautogui.click(-50,1050)
                sleep(0.01)
                pyautogui.press('esc')
                pyautogui.click(-648,659)

    pyautogui.click(-350,20) #clicks Chrome Window
    pyautogui.click(960,505) #Back to main screen
    print("Done Exiting Games")

def on_press_f6():
    global game_number
    game_number += 1
#Main Loop:

#listen for F8 Debug Press
keyboard.add_hotkey('F8', debug_mouse_position)

#listen for 'F3' press
keyboard.add_hotkey('F3', on_press_f3)
#listen for 'F4' New Game Press
keyboard.add_hotkey('F4', on_press_f4)
#listen for 'F5' Exit press
keyboard.add_hotkey('F5', on_press_f5)
#listen fo 'F6' Key Press
keyboard.add_hotkey('F6', on_press_f6)

#keep program running to listen for the key press
keyboard.wait('F7')