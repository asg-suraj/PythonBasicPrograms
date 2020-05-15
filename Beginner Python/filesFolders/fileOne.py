#module for file handelling
import os


print(os.path.join('folder1','folder2','folder3','folder4')) 
# will get folder1\folder2\folder3\folder4 because of windows os 
#in mac or linux folder1/folder2/folder3/folder4 i.e use of forward slash
# to see which of this slash it may use type print(os.sep) on python terminal

#to see In which Directory The python program running is 
print(os.getcwd())

#now to change the Directory from program u write
os.chdir('S:\\Acadmecis College\\Programming\\Beginner Python') # \\ is used to Escape \
#let's see if the Directory is changed or not
print(os.getcwd())

# To check Absolute file path (like this-)S:\Acadmecis College\Programming\Beginner Python\filesFolders
print(os.path.abspath(os.getcwd())) #will return absolute path for provided path (here os.getcwd() is provided)
print(os.path.abspath('..\\')) #it actually means parent folder of current working Directory
#also 
print(os.path.abspath('..\\..\\'))#parent of parent
#and
print(os.path.isabs(os.getcwd())) #will print True as it is the absolute path
#try some functions like os.path.relpath() , os.path.dirname() , os.path.basename()

#also
print(os.path.exists('c:\\folder1\\folder2\\spam.png'))   #as it does not exist so False
print(os.path.isfile('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders'))  #False
print(os.path.isfile('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders\\fileOne.py'))  #True cause it's a file
print(os.path.isdir('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders'))   #True because it is directory


#To get file/folder size
print(os.path.getsize('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders\\fileOne.py'))   #Size in bytes

#to get all files and folders
#print(os.listdir('c:\\')) #will print names of all folders in C:\Users

#small code to get all files Size and the total size of all 
DirList=os.listdir('c:\\')
os.chdir('c:\\')
totalsize=0

for i in DirList:   #will take each file and folder of os.getcwd() #Current Folder  and store in i
	print(i+'								',end='') # will print next output on same line due to  end=''
	print(os.path.getsize(i),end='') #will print Size
	print(' bytes')
	totalsize=totalsize+os.path.getsize(i)
print('total Size of The C:\\Users is ',end='')
print(totalsize,end='')
print(' bytes')

#To Create folders and Sub folders
os.makedirs('S:\\Acadmecis College\\Programming\\Beginner Python\\filesFolders\\created\\folder\\using\\makedirs\\function')   #can provide Absolute or releative paths
