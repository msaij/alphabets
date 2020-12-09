import os
import tkinter
from tkinter import *
import pyautogui

folderofpic="C:/Users/SpectrusRage/3D Objects/alphabets/oneimg_ss"
def onlyoneimgcheck():
    if len(os.listdir(folderofpic))>1:
        print("There are mulitple files in "+os.path.basename(folderofpic)+". We are removing the files which are not '.png' as listed below.")
        for imgorfldr in os.listdir(folderofpic):
            if not imgorfldr.endswith('theimage.png'):
                print(imgorfldr)
                os.rmdir(os.path.join(folderofpic,imgorfldr))
def saveimg():
    imgpath=os.path.join(folderofpic,"theimage.png")
    myScreenshot.save(imgpath)

onlyoneimgcheck()
myScreenshot = pyautogui.screenshot() #screenshot is taken and saved in myScreenshot
saveimg()
