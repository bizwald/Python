# logic source: 
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join
mypath = "F:\\SBAC\\16-17\\ETS_CA\\XML\\EL3"
filelist = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(filelist)