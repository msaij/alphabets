import os
import tkinter
from tkinter import *
import pyautogui

folderofpic="C:/Users/SpectrusRage/3D Objects/alphabets/alphabets_ss"
def checkingfileforextras():
    #  This function checks if there are multiple images or other files in folderofpic,
    #  to ensure that there is only one imagE.
    if len(os.listdir(folderofpic))>1:
        print("There are mulitple files in "+os.path.basename(folderofpic)+". We are removing the files which are not '.png' .")
        for imgorfldr in os.listdir(folderofpic):
            if not imgorfldr.endswith('.png'):
                os.rmdir(os.path.join(folderofpic,imgorfldr))

checkingfileforextras()
myScreenshot = pyautogui.screenshot() #screenshot is taken and saved in myScreenshot

def getnof():  #get name of file - getnof
    img=nof.get()
    imgname=img+".png"
    imgpath=os.path.join(folderofpic,imgname)
    if bool(os.path.isfile(imgpath)):
        print("We already have a file with this name, "+imgname+". And you can save only one image")
        filename_tk.destroy()
    elif bool(not os.path.isfile(imgpath)) & len(os.listdir(folderofpic))==1 or len(os.listdir(folderofpic))>1:
        print("We already have an image so cannot create "+imgname+".")
        filename_tk.destroy()
    else:
        myScreenshot.save(imgpath)
        print("Your image "+imgname+" is saved.")
        filename_tk.destroy()

filename_tk = tkinter.Tk() # Tkinter filename_tk start
nofq = Label(filename_tk, text="Name of the file:")
nofq.grid(row=0)
nof = Entry(filename_tk)
nof.grid(row=1)
submit_filename = Button(filename_tk, text="Submit", width=10, command=getnof) # Tkinter callback command
submit_filename.grid(row=2)
filename_tk.mainloop() # Tkinter filename_tk ending
