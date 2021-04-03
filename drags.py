import os
import stat
import psutil
import subprocess
def security_pic_check():
    if os.path.exists(os.path.join(".","oneimg_ss","security_pic.png")):
        if os.path.exists(os.path.join(".","lockfolder")):
            return 0 #if 0 is returned it means that security_pic and lockfolder exists



# if not os.startfile(os.path.join(".","lockfolder")).closed():
#    print("scma")
process=subprocess.Popen(f'explorer {os.path.realpath(os.path.join(".","lockfolder"))}')
while process.poll()==None:
    print("polling")
print("polling f")

os.startfile(os.path.join(".","lockfolder"))

p=subprocess.call(os.path.join(".","lockfolder"))
