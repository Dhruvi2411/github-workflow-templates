import os
import time

def clear_terminal():
    # 'nt' refers to Windows; 'posix' covers Mac and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

print("This text will disappear.")
time.sleep(2)

clear_terminal()
print("The screen is now clear!")
