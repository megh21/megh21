#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import shutil
from datetime import datetime
goodtogo1=False
goodtogo2=False

while(not(goodtogo1 and goodtogo2)):
    if not goodtogo1: 
        pathIn=str(input("give input path"))
    
    try:
        if(os.path.lexists(pathIn)):
            goodtogo1=True
            pathOut=str(input("give output path"))
            try:
                if(os.path.lexists(pathOut)):
                    goodtogo2=True
                else:
                    print("invalid Input 2 here")
            except:
                print("invalid Input 2")
        else:
            print("invalid Input 1 here")
      
    except:
        print("invalid Input 1")
        
        
dirList=os.listdir(pathIn)
print(dirList)
def getDate(file):
    os.chdir(pathIn)
    timeStamp=os.stat(str(file)).st_mtime
    dateString=str(datetime.fromtimestamp(timeStamp))
    return dateString

def parseDate(date):
    year=date[:4]
    mon=date[5:7]
    monthDir={'01':"Jan",'02':"Feb",'03':"Mar",'04':"Apr",
              '05':"May",'06':"Jun",'07':"Jul",'08':"Aug",
              '09':"Sep",'10':"Oct",'11':"Nov",'12':"Dec"} 
    if mon in monthDir:
        monthStr= monthDir.get(mon)           
    combineName=monthStr+year
    return combineName

def createFolder(Name):
    newFolder=pathOut+ r"/"+ Name
    if os.path.isdir(newFolder):
        #print("in if")
        pass
    else:
        os.mkdir(newFolder)
        #print("os.mkdirelse")
    return newFolder 


    
for file in dirList:
    if "." in file:
        #print("file",file)
        Date=getDate(file)
        #print("date",Date) 
        Name=parseDate(Date)
        #print("folder",Name) 
        newFolder=createFolder(Name)
        #print(newFolder)
        if file is not newFolder:
            try:
                shutil.move(file,newFolder)
        
                print("it is moved!")
            except:
                print("cannot move in itself")
        #print()

