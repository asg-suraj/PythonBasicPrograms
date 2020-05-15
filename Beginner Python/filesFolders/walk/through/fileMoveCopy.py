import os
import shutil  #it is used to copy paste stuff

#Note in (this is source , this is destination)

#shutil.copy() funnction used to copy the files
shutil.copy('mydata.bak','created\\folder\\using\\makedirs') #both address are releative address to current directory
#shutil.copy() will copy mydata.bak to created\\folder\\using\\makedirs

#we can copy and rename at the Same time
shutil.copy('mydata.bak','created\\folder\\using\\makedirs\\mydataNameChange.d') #both address are releative address to current directory
#this command will save mydata.bak renamed as mydataNameChange.d at specified address 


#shutil.copytree() is used to copy folder from source to destination
shutil.copytree('S:\\Acadmecis College\\Programming\\Beginner Python', 'S:\\Acadmecis College\\Placement\\pythonProgs1') #if folder is not there it will create the folder and then copy all folder of source to destination

#shutil.move() used for moving the file 
shutil.move('created\\folder\\using\\makedirs\\mydataNameChange.bak',os.getcwd()) #will move mydataNameChange.bak to current Directory

