import os

def fc():
    filescountpath=os.listdir("C:/Users/SpectrusRage/3D Objects/alphabets/oneimg_ss")
    filescount=0
    for a_file in filescountpath:
        filescount+=1
    return filescount

filescount=fc()
if filescount==1:
    print("swipe code")
else:
    os.system("python alphabets_main.py")
