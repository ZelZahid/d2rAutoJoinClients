#Python script/program that AUTO-joins / creates/ leaves Diablo 2 - Resurrected games in Online Battle.net for the 
# purpose of increasing player count. Clients on other monitors must be windowed mode and placed in specific areas.
#Instructions: After placing clients on specific locations on screens,
# F3 --> Join Game
# F4 --> New Game, [leaves game from all clients, then creates/join a game with all clients]
# F5 --> Exists all additional clients, Not the main client.
# F6 --> Changes Game number += 1
# Todo: Combine both versions of AutoJoinClient, [Main + Computer#2]
from time import sleep, time
import keyboard
import pyautogui
import sys

# === GLOBAL SETTINGS ===
click_delay = 0.12  # Change this to set global delay between mouse actions

# === SAFE FUNCTIONS ===
def safe_click(x, y):
    #pyautogui.click(x, y) #may have caused crashes
    pyautogui.moveTo(x, y,duration=0.1) #smoother mouse movement
    pyautogui.click()
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
game_name = "zel"
game_password = "123"
game_number = 1
numOfAccounts = 3

client1_window_loc = 5 #unused variable
#Enter Client Locations here:
client2_window_loc = (2200, 20)  # Account 2
client2_joingametab_loc = (2900, 90)
client2_joingamename_loc = (2800, 136)
client2_joingamepass_loc = (3000, 136)
client2_saveandexit_loc = (2562, 362)  # Save and Exit for Account 2

client3_window_loc = (3800, 1037)  # Account 3
client3_joingametab_loc = (3550, 384)
client3_joingamename_loc = (3450, 460)
client3_joingamepass_loc = (3600, 460)
client3_saveandexit_loc = (3200, 658)  # Save and Exit for Account 3

#4th Account
client4_window_loc = (3500, 20)   # Account 4
client4_joingametab_loc = (3540, 84)
client4_joingamename_loc = (3430, 131)
client4_joingamepass_loc = (3618, 131)
client4_saveandexit_loc = (3180, 348)  # Save and Exit for Account 4

#5th Account
client5_window_loc = (2000, 1020) # Account 5
client5_joingametab_loc = (2880, 390)
client5_joingamename_loc = (2880, 460)
client5_joingamepass_loc = (3000, 460)
client5_saveandexit_loc = (2562, 658)  # Save and Exit for Account 5

#6th Account
client6_window_loc = (-1874, 1000) # Account 6
client6_joingametab_loc = (-965, 382)
client6_joingamename_loc = (-965, 455)
client6_joingamepass_loc = (-871, 455)
client6_saveandexit_loc = (-871, 658)  # Save and Exit for Account 6

#7th Account
client7_window_loc = (-1700, 15)  # Account 7
client7_joingametab_loc = (-1700, 90)
client7_joingamename_loc = (-1800, 136)
client7_joingamepass_loc = (-1700, 136)
client7_saveandexit_loc = (-1710, 362)  # Save and Exit for Account 7

#8th Account
client8_window_loc = (-50, 1050)  # Account 8
client8_joingametab_loc = (-50, 90)
client8_joingamename_loc = (-150, 136)
client8_joingamepass_loc = (-50, 136)
client8_saveandexit_loc = (-60, 362)  # Save and Exit for Account 8

def on_press_f3():
    global game_number
    game_number_str = str(game_number)
    print("JOINING GAME:", game_name, game_number)

    if numOfAccounts >= 2:
        # Account 2
        safe_click(client2_window_loc[0], client2_window_loc[1])
        safe_click(client2_joingametab_loc[0], client2_joingametab_loc[1])
        safe_click(client2_joingamename_loc[0], client2_joingamename_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(client2_joingamepass_loc[0], client2_joingamepass_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

    if numOfAccounts >= 3:
        # Account 3
        safe_click(client3_window_loc[0], client3_window_loc[1])
        safe_click(client3_joingametab_loc[0], client3_joingametab_loc[1])
        safe_click(client3_joingamename_loc[0], client3_joingamename_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(client3_joingamepass_loc[0], client3_joingamepass_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

    if numOfAccounts >= 4:
        # Account 4
        safe_click(client4_window_loc[0], client4_window_loc[1])
        safe_click(client4_joingametab_loc[0], client4_joingametab_loc[1])
        safe_click(client4_joingamename_loc[0], client4_joingamename_loc[1] )
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(client4_joingamepass_loc[0], client4_joingamepass_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')
    if numOfAccounts >= 5:
        # Account 5
        safe_click(client5_window_loc[0], client5_window_loc[1])
        safe_click(client5_joingametab_loc[0], client5_joingametab_loc[1])
        safe_click(client5_joingamename_loc[0], client5_joingamename_loc[1])
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_name + game_number_str)
        safe_click(client5_joingamepass_loc[0], client5_joingamepass_loc[1] )
        safe_hotkey('ctrl', 'a')
        safe_press('backspace')
        safe_write(game_password)
        safe_press('enter')

        if numOfAccounts >= 7:
            # Account 6
            safe_click(client6_window_loc[0], client6_window_loc[1])
            safe_click(client6_joingametab_loc[0], client6_joingametab_loc[1])
            safe_click(client6_joingamename_loc[0], client6_joingamename_loc[1])
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_name + game_number_str)
            safe_click(client6_joingamepass_loc[0], client6_joingamepass_loc[1])
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_password)
            safe_press('enter')

            # Account 7
            safe_click(client7_window_loc[0], client7_window_loc[1])
            safe_click(client7_joingametab_loc[0], client7_joingametab_loc[1])
            safe_click(client7_joingamename_loc[0], client7_joingamename_loc[1])
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_name + game_number_str)
            safe_click(client7_joingamepass_loc[0], client7_joingamepass_loc[1])
            safe_hotkey('ctrl', 'a')
            safe_press('backspace')
            safe_write(game_password)
            safe_press('enter')

            if numOfAccounts == 8:
                # Account 8
                safe_click(client8_window_loc[0], client8_window_loc[1])
                safe_click(client8_joingametab_loc[0], client8_joingametab_loc[1])
                safe_click(client8_joingamename_loc[0], client8_joingamename_loc[1])
                safe_hotkey('ctrl', 'a')
                safe_press('backspace')
                safe_write(game_name + game_number_str)
                safe_click(client8_joingamepass_loc[0], client8_joingamepass_loc[1])
                safe_hotkey('ctrl', 'a')
                safe_press('backspace')
                safe_write(game_password)
                safe_press('enter')

    # Return mouse to center screen
    safe_click(-350, 20)
    #safe_click(2200, 20)
    #safe_click(960, 505)#replace with move mouse
    pyautogui.moveTo(960, 505,duration=0.05) #smoother mouse movement
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

def on_press_f5():
    if numOfAccounts >= 2:
        print("EXIT init()")
        safe_click(client2_window_loc[0], client2_window_loc[1])
        safe_press('esc')
        safe_click(client2_saveandexit_loc[0], client2_saveandexit_loc[1])
    if numOfAccounts >= 3:
        safe_click(client3_window_loc[0], client3_window_loc[1])
        safe_press('esc')
        safe_click(client3_saveandexit_loc[0], client3_saveandexit_loc[1])
    if numOfAccounts >= 4:
        safe_click(client4_window_loc[0], client4_window_loc[1])
        safe_press('esc')
        safe_click(client4_saveandexit_loc[0], client4_saveandexit_loc[1])
    if numOfAccounts >= 5:
        safe_click(client5_window_loc[0], client5_window_loc[1])
        safe_press('esc')
        safe_click(client5_saveandexit_loc[0], client5_saveandexit_loc[1])
        if numOfAccounts >= 7:
            safe_click(client6_window_loc[0], client6_window_loc[1])
            safe_press('esc')
            safe_click(client6_saveandexit_loc[0], client6_saveandexit_loc[1])
            safe_click(client7_window_loc[0], client7_window_loc[1])
            safe_press('esc')
            safe_click(client7_saveandexit_loc[0], client7_saveandexit_loc[1])
            if numOfAccounts == 8:
                safe_click(client8_window_loc[0], client8_window_loc[1])
                safe_press('esc')
                safe_click(client8_saveandexit_loc[0], client8_saveandexit_loc[1])
    safe_click(-350, 20)
    #safe_click(960, 505) #replace with move mouse pos
    pyautogui.moveTo(960, 505,duration=0.05) #smoother mouse movement
    print("Done Exiting Games")

def on_press_f6():
    global game_number
    game_number += 1
    print("game number is Now:", game_number)

# === HOTKEYS ===
keyboard.add_hotkey('F3', on_press_f3)
keyboard.add_hotkey('F4', on_press_f4)
keyboard.add_hotkey('F5', on_press_f5)
keyboard.add_hotkey('F6', on_press_f6)
keyboard.add_hotkey('F8', debug_mouse_position)
keyboard.add_hotkey('F12', emergency_exit)  # Safety escape

# === MAIN LOOP ===
keyboard.wait('F7')
