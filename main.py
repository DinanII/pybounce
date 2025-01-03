from Game import Game
from Helper import Helper
import time
import sys
isRunning = True

while isRunning:
    Helper.clearConsole()
    print("===========================================",end="\n\n")
    print("PyBounce",end="\n\n")
    print("===========================================")
    print("0. Quit")
    print("1. Start Game")
    choice = Helper.askForString("Make a choice")
    match choice:
        case "0":
            sys.exit(0)
        case "1":
            print("Game will launce in a moment")
            time.sleep(1.5)
            Helper.clearConsole()
            Game('Bounce Game')
        case _:
            print("Invalid option")
            Helper.waitForUser()
#https://realpython.com/python-gui-tkinter/
#   python3 pyinstaller --onefile --add-binary /usr/lib/x86_64-linux-gnu/libpython3.12.so.1.0:. main.py
#   wine python -m PyInstaller --onefile --add-binary /usr/lib/x86_64-linux-gnu/libpython3.12.so.1.0:. main.py
