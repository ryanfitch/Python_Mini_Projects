# txtFileTransferByTime.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7
# This is a Python program which moves .txt files from one folder to another only if the file isn't already there. 

import shutil
import os
import datetime as dt

def copyFile(src, dst):
    # sets current time to a variable
    now = dt.datetime.now()
    # sets the time 24 hours ago to a variable
    ago = now-dt.timedelta(minutes=1440)

    # looks in the source folder which was passed in
    for file in os.listdir(src):
         # creates new variable with the full path name to the file
         full_path = os.path.join(src, file)
         # sets time stamp to each file to the mtime variable
         st = os.stat(full_path)
         mtime = dt.datetime.fromtimestamp(st.st_mtime)
         # checks to see which files have been edited in the last day by comparing the file time stamps to the 'ago' variable who's value is one day
         # copies files if file has been modified within one days time and displays the status of what was copied
         if mtime > ago:
             # checks to make sure only .txt files are being copied
             if file.lower().endswith(('.txt')):    
                 shutil.copy(full_path, dst)
                 print('%s modified %s'%(src +file, mtime))

copyFile("/Users/ryanfitch/Desktop/FolderA/", "/Users/ryanfitch/Desktop/FolderB/")
