import os
from os import path
import pyautogui
import tkinter as tk
from tkinter import messagebox

folderofpic="C:/Users/SpectrusRage/3D Objects/alphabets/oneimg_ss"
imgname="security_pic.png"

def excptmainimg_del_evryothrfile(): #this function is being complied in mainfn_saveandcheck
    for thefile in os.listdir(folderofpic):
        if thefile==imgname:
            pass
        else:
            try:
                os.remove(os.path.join(folderofpic,thefile))
            except:
                os.rmdir(os.path.join(folderofpic,thefile))

def saveimg(): #this function is being complied in mainfn_saveandcheck
    print("Pick an image you want as your screen lock")
    myScreenshot = pyautogui.screenshot() #screenshot is taken and saved in myScreenshot
    imgpath=os.path.join(folderofpic,imgname)
    myScreenshot.save(imgpath)
    print("Success.")

def createlockappfolder(): #this function is being complied in mainfn_saveandcheck
    try:
        lckfldr="lockfolder"
        lckfldrpath=os.path.join(".",lckfldr)
        os.mkdir(lckfldrpath,0o666)
    except:
        pass

def mainfn_saveandcheck():
    if len(os.listdir(folderofpic))==0:
        saveimg()
    else:
        excptmainimg_del_evryothrfile()
        if len(os.listdir(folderofpic))==0:
            saveimg()
    createlockappfolder()

mainfn_saveandcheck()
# Running the mainfn_saveandcheck() which has createlockappfolder(),saveimg() and excptmainimg_del_evryothrfile()

p=tk.Tk()
p.attributes('-alpha',0)
messagebox.showinfo("TwoSwipe", "Place a file or a folder in 'lockfolder' folder to secure it.")
