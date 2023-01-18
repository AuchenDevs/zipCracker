from pyzipper import AESZipFile

from os import system, getcwd, access, W_OK
from datetime import datetime
from tkinter import filedialog, Tk
from threading import Thread
from time import sleep
from concurrent.futures import ThreadPoolExecutor

tries = 0

system("title ZiPCracker")
#Helpers
def cls():
    system("cls")

def title():
    while True:
        system(f"title {tries}")
        sleep(0.1)
        
        
#Main
def crack(file, wordlist):
    global tries
    cls()
    tries = 0
    foldername = file.name.split("/")[-1]
    foldername = foldername.split(".")[0]
    Thread(target=title,).start()
    startTime = datetime.now()
    with open(wordlist.name, encoding="latin-1") as f:
        for line in iter(f.readline, ''):
            word = line.strip()
            try: 
                with AESZipFile(file.name, "r") as z:
                    z.extractall(foldername, pwd=bytes(word, 'utf-8'))
            except:
                tries += 1
            else:
                found = True
                break
            
    if not found:
        print("The password was not found. Try using another wordlist")
    else: 
            print(f"The password was found. It is \"{word}\", it was found at the try {tries} and it took {(datetime.now() - startTime).total_seconds()}")
            system(f"explorer \"{getcwd()}\\{foldername}\"")

root = Tk()
root.withdraw()
print("What file do you want to crack")
file = filedialog.askopenfile(mode='r', title="Select a file to crack", initialdir=getcwd(), filetypes=(("Zip file", ".zip"),))
print("Select your wordlist (If you don't have search for \"Rockyou\")")
wordlist = filedialog.askopenfile(mode='r', title="Wordlist", initialdir=getcwd(), filetypes=(("Text files", ".txt"),))

try:
    crack(file, wordlist)
    print("Program stopped")
    system("pause >nul")
except KeyboardInterrupt:
    print("leaving")
    sleep(2)
