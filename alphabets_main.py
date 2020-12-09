import os
from os import path
import pyautogui

folderofpic="C:/Users/SpectrusRage/3D Objects/alphabets/oneimg_ss"
imgname="theoneandonlyimg.png"

def excptmainimg_del_evryothrfile():
    for thefile in os.listdir(folderofpic):
        if thefile==imgname:
            pass
        else:
            try:
                os.remove(os.path.join(folderofpic,thefile))
            except:
                os.rmdir(os.path.join(folderofpic,thefile))

def saveimg():
    print("Which image you want as your screen lock")
    myScreenshot = pyautogui.screenshot() #screenshot is taken and saved in myScreenshot
    imgpath=os.path.join(folderofpic,imgname)
    myScreenshot.save(imgpath)
    print("Success.")

def mainfn_saveandcheck():
    if len(os.listdir(folderofpic))==0:
        saveimg()
    else:
        excptmainimg_del_evryothrfile()
        if len(os.listdir(folderofpic))==0:
            saveimg()

mainfn_saveandcheck() # Running the main function which has both saveimg() and excptmainimg_del_evryothrfile()
