import os


helloFile=open('hello.txt') #here given Releative path you can give absolute path also (here hello.txt is in same directory)

print(helloFile.read()) #text in hello.txt
print(helloFile.read()) #it will not read second time i.e you need to open again
#to not reading again we will store it in variable
helloFile=open('hello.txt') 
filecontent=helloFile.read()
print(filecontent)
print(filecontent)


#readline method
helloFile=open('hello.txt')
p=helloFile.readlines()
print(p)
helloFile.close()



#opening Files in write mode
helloFile=open('hello2.txt','w') #w indicates write mode and if file not exist it will create new file with given name

helloFile.write('Hello !!!!!!!\n')
helloFile.write('Hello !!!!!!!')
helloFile.close()  #closing after job is done

helloFile=open('hello2.txt') #to read we have to open it in read mode
print(helloFile.read())
helloFile.close()


#opening in append mode
helloFile=open('hello.txt','a') #a indicates append mode
helloFile.write('\n \n My name is Shri') #will append this String to orignal hello.txt
helloFile.close()

#check appended Document
helloFile=open('hello.txt')
filecontent=helloFile.read()
print(filecontent)
helloFile.close()


#shelve module -- to save  different types variables,list, dictionaries in binary shelve files
import shelve
shelvFile= shelve.open('mydata') #it first time create three files mydata.bak , mydata.dat , mydata.dir
shelvFile['friends']=['joey','chandler','ross','rachel','pheobe','monica'] #it is sort of dictionary like structure i.e friends is a key and their names are values

shelvFile.close()

shelvFile=shelve.open('mydata')
print(shelvFile['friends'])
print(list(shelvFile.keys())) #it will print key that is friends
print(list(shelvFile.values())) #it will print values that is names
shelvFile.close()



















