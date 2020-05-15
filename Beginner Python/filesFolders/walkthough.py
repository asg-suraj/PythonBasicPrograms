#this walk means whatever applied to main folder will apply to all files and folders inside main folder
import os , shutil

#this is used for walkthough
for folderName , subfolders , filenames in os.walk('walk'): #need to write in this way only
	print('The folder is '+ folderName)
	print('The subfolders in '+folderName + ' are: '+str(subfolders))
	print('The files in '+folderName + ' are: '+str(filenames)+'\n')


#we can use this as
#to delete any folder with name 'fish' for Example

for subfolder in subfolders:
	if subfolder=='fish':
		os.unlink(subfolder)

for file in filenames:
	if file.endswith('.py'):
		shutil.copy(os.path.join(folderName,file), os.path.join(folderName, file+'.txt'))
