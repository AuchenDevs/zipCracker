import pyzipper

import os
from datetime import datetime

import tkinter as tk
from tkinter import filedialog
import threading
import time

tries = 0

os.system("title ZiPCracker")
#Helpers
def cls():
    os.system("cls")

def title(total):
    while True:
        os.system(f"title {tries}/{total}")
        time.sleep(0.00001)
#Main
def crack(file, wordlist):
    global tries
    cls()
    print("Loading Wordlist")
    words = []
    
    os.system("title Loading wordlist")
    wordlistsize = 0
    startTime = datetime.now()
    with open (wordlist.name, "r", encoding="latin-1") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            wordlistsize += 1
            words.append(line)
    print(f"Word list loaded. Took: {(datetime.now() - startTime).total_seconds()}")
    foldername = file.name.split("/")[-1]
    foldername = foldername.split(".")[0]
    x = threading.Thread(target=title, args=(str(wordlistsize),))
    x.start()
    for word in words:
        try: 
            with pyzipper.AESZipFile(file.name, "r") as z:
                z.extractall(foldername, pwd=bytes(word, 'utf-8'))
        except PermissionError:
            print("I don't have permission to create a folder here!")
            return
        except:
            tries += 1
        else:
            print(f"The password was found. It is \"{word}\" and it was found at the try {tries}")
            os.system(f"explorer \"{os.getcwd()}\\{foldername}\"")
            return
    print("The password was not found. Try using another wordlist")
root = tk.Tk()
root.withdraw()
print("What file do you want to crack")
file = filedialog.askopenfile(mode='r', title="Select a file to crack", initialdir=os.getcwdb(), filetypes=(("Zip file", ".zip"),))
print(file)
print("Select your wordlist (If you don't have search for \"Rockyou\")")
wordlist = filedialog.askopenfile(mode='r', title="Wordlist", initialdir=os.getcwdb(), filetypes=(("Text files", ".txt"),))
try:
    crack(file, wordlist)
    print("Program stopped")
    os.system("pause >nul")
except KeyboardInterrupt:
    print("leaving")
    time.sleep(2)
