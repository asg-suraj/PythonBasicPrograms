import os

#os.rmdir() is used to delete folders if the Directory is completely Empty
os.makedirs('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders\\foldertoDelete')   #can provide Absolute or releative paths
os.rmdir('foldertoDelete') #will delete the given folder as it was created by above line it was empty

#to delete The Folder with content
import shutil
#os.makedirs('S:\\Acadmecis College\\Placement\\pythonProgs1') #command to use for creating folder
#shutil.rmtree('S:\\Acadmecis College\\Placement\\pythonProgs1') #will delete this folder
#be careful while using these command this will remove folder permantly

os.chdir('created\\folder\\using\\makedirs')

for filename in os.listdir():
	if filename.endswith('.d'):
		#print(filename)
		os.unlink(filename) #this command will delete all files with extension
		#here mydataNameChange.d got deleted


#This above deletion is somewhat Dangerous cause can delete Imp files permanantly 
#so there is module which will delete to recycle bin only
# that is send2trash
import send2trash

os.makedirs(os.path.join(os.getcwd(),'foldertoDeleteUsingSend2Trash')) #creates folder

#send2trash.send2trash('folderToDelete')

send2trash.send2trash('foldertoDeleteUsingSend2Trash') #sends to Recycle Bin