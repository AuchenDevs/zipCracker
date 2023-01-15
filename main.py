import os
import threading
from time import sleep
from datetime import datetime

from pyzipper import AESZipFile
from tkinter import filedialog

tries = 0

os.system("title ZiPCracker")

#Helpers
def cls():
    os.system("cls")

def title(total):
    while True:
        os.system(f"title {tries}/{total}")

#Main
def crack(file, wordlist):
    global tries
    cls()
    print("Loading Wordlist")
    os.system("title Loading wordlist")
    
    startTime = datetime.now()
    words = open(wordlist.name, 'r').read()
    words = words.split('\n')
    wordlistsize = len(words)

    print(f"Word list loaded. Took: {(datetime.now() - startTime).total_seconds()}ms")
    foldername = file.name.split("/")[-1]
    foldername = foldername.split(".")[0]
    threading.Thread(target=title, args=(str(wordlistsize),)).start()
    print('password selection started')
    for word in words:
        try: 
            with AESZipFile(file.name, "r") as z:
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


if __name__ == '__main__':
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
        sleep(2)
