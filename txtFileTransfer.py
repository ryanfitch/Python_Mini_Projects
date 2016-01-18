# txtFileTransfer.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7. 
# This is a Python program which moves .txt files from one folder to another only if the file isn't already there. 


import shutil
import os

# sets folder source to move files from
for root, dirs, files in os.walk(r'/Users/ryanfitch/Desktop/FolderA/'):
    for ckfile in files:
        for root2, dirs2, files2 in os.walk(r'/Users/ryanfitch/Desktop/FolderB/'):
            # checks to make sure files aren't already in the new folder
            if ckfile not in files2:
                # checks for .txt files and only moves those files
                if ckfile.lower().endswith(('.txt')):
                    # lets user know which files have successfully moved
                    print"Moving "+ckfile+" to back up folder."
                    copyf = os.path.join(root,ckfile)
                    shutil.move(copyf, r'/Users/ryanfitch/Desktop/FolderB/')    
            else:
                # lets user know which files are already in the new folder
                print "The file "+ckfile+" is already backed up"
