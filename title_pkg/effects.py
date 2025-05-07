import sys
import time

def typewriter(text, delay=0.00):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')