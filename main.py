#Python script/program that AUTO-joins / creates/ leaves Diablo 2 - Resurrected games in Online Battle.net for the 
# purpose of increasing player count. Clients on other monitors must be windowed mode and placed in specific areas.
#Instructions: After placing clients on specific locations on screens,
# F3 --> Join Game
# F4 --> New Game, [leaves game from all clients, then creates/join a game with all clients]
# F5 --> Exists all additional clients, Not the main client.
# F6 --> Changes Game number += 1
from time import sleep, time
import keyboard
import pyautogui
import sys

# === GLOBAL SETTINGS ===
click_delay = 0.1  # Change this to set global delay between mouse actions

# === SAFE FUNCTIONS ===
def safe_click(x, y):
    pyautogui.click(x, y)
    sleep(click_delay)

def safe_write(text):
    pyautogui.write(text)
    sleep(click_delay)

def safe_hotkey(*args):
    pyautogui.hotkey(*args)
    sleep(click_delay)

def safe_press(key):
    pyautogui.press(key)
    sleep(click_delay)

# === EMERGENCY EXIT ===
def emergency_exit():
    print("Emergency exit triggered. Exiting script.")
    sys.exit()

# === MOUSE DEBUG ===
def debug_mouse_position():
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: (X: {x}, Y: {y})")
        sleep(0.2)

# === MAIN FUNCTIONS ===
game_name = "Zaz"
game_password = "123"
game_number = 1
numOfAccounts = 3

def on_press_f3():
    global game_number
    game_number_str = str(game_number)
    print("JOINING GAME:", game_name, game_number)

    # Account 1
    safe_click(2200, 20)
    safe_click(2900, 90)
    safe_click(2800, 136)
    safe_hotkey('ctrl', 'a')
    safe_press('backspace')
    safe_write(game_name + game_number_str)
    safe_click(3000, 136)
    safe_hotkey('ctrl', 'a')
    safe_press('backspace')
    safe_write(game_password)
    safe_press('enter')

    if numOfAccounts >= 3:
        # Account 2
        safe_click(3500, 925)
        safe_click(3550, 384)
        safe_click(3450, 460)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(3600, 460)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

    if numOfAccounts >= 5:
        # Account 3
        safe_click(3500, 20)
        safe_click(3553, 90)
        safe_click(3450, 136)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(3650, 136)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

        # Account 4
        safe_click(2000, 1020)
        safe_click(2880, 390)
        safe_click(2880, 460)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(3000, 460)
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

        if numOfAccounts >= 7:
            # Account 5
            safe_click(-1874, 1000)
            safe_click(-965, 382)
            safe_click(-965, 455)
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_name + game_number_str)
            safe_click(-871, 455)
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_password)
            safe_press('enter')

            # Account 6
            safe_click(-1700, 15)
            safe_click(-970, 85)
            safe_click(-970, 136)
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_name + game_number_str)
            safe_click(-857, 136)
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_password)
            safe_press('enter')

            if numOfAccounts == 8:
                # Account 7
                safe_click(-50, 1050)
                safe_click(-295, 385)
                safe_click(-392, 455)
                safe_hotkey('ctrl', 'a')
                safe_press('backspace')
                safe_write(game_name + game_number_str)
                safe_click(-200, 455)
                safe_hotkey('ctrl', 'a')
                safe_press('backspace')
                safe_write(game_password)
                safe_press('enter')

    # Return mouse to center screen
    safe_click(-350, 20)
    safe_click(2200, 20)
    safe_click(960, 505)
    print("Done Joining")

def on_press_f4():
    global game_number
    print("NEW GAME!:", game_name, game_number)
    safe_press('esc')
    safe_click(960, 475)
    sleep(click_delay)
    on_press_f5()

    # Create new game
    game_number += 1
    game_number_str = str(game_number)
    safe_click(1273, 80)
    safe_click(1450, 175)
    safe_hotkey('ctrl', 'a')
    safe_press('backspace')
    safe_write(game_name + game_number_str)
    safe_click(1430, 245)
    safe_hotkey('ctrl', 'a')
    safe_press('backspace')
    safe_write(game_password)
    safe_press('enter')
    sleep(click_delay)
    on_press_f3()
    sleep(click_delay)
    safe_press('alt')

def on_press_f5():
    print("EXIT init()")
    safe_click(2200, 20)
    safe_press('esc')
    safe_click(2562, 362)
    if numOfAccounts >= 3:
        safe_click(3500, 925)
        safe_press('esc')
        safe_click(3200, 658)
    if numOfAccounts >= 5:
        safe_click(3500, 20)
        safe_press('esc')
        safe_click(3200, 360)
        safe_click(2000, 1020)
        safe_press('esc')
        safe_click(2560, 664)
        if numOfAccounts >= 7:
            safe_click(-1874, 1000)
            safe_press('esc')
            safe_click(-1284, 660)
            safe_click(-1700, 15)
            safe_press('esc')
            safe_click(-1284, 360)
            if numOfAccounts == 8:
                safe_click(-50, 1050)
                safe_press('esc')
                safe_click(-648, 659)
    safe_click(-350, 20)
    safe_click(960, 505)
    print("Done Exiting Games")

def on_press_f6():
    global game_number
    game_number += 1

# === HOTKEYS ===
keyboard.add_hotkey('F3', on_press_f3)
keyboard.add_hotkey('F4', on_press_f4)
keyboard.add_hotkey('F5', on_press_f5)
keyboard.add_hotkey('F6', on_press_f6)
keyboard.add_hotkey('F8', debug_mouse_position)
keyboard.add_hotkey('F12', emergency_exit)  # Safety escape

# === MAIN LOOP ===
keyboard.wait('F7')
