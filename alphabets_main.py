import os
import pyautogui

folderofpic="C:/Users/SpectrusRage/3D Objects/alphabets/oneimg_ss"
imgname="theoneandonlyimg.png"

def onlyoneimgcheck():
    for thefile in os.listdir(folderofpic):
        if thefile==imgname:
            pass
        else:
            try:
                os.remove(os.path.join(folderofpic,thefile))
            except:
                os.rmdir(os.path.join(folderofpic,thefile))

def saveimg():
    myScreenshot = pyautogui.screenshot() #screenshot is taken and saved in myScreenshot
    imgpath=os.path.join(folderofpic,imgname)
    myScreenshot.save(imgpath)
    print("Success.")

def mainfn_saveandcheck():
    if len(os.listdir(folderofpic))==0:
        saveimg()
    else:
        onlyoneimgcheck()
        if len(os.listdir(folderofpic))==0:
            saveimg()

mainfn_saveandcheck() # Running the main function which has both saveimg() and onlyoneimgcheck()
