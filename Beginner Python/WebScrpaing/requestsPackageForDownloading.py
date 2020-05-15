import requests,os

res=requests.get('http://automatetheboringstuff.com/files/rj.txt') #response object is stored in res variable
print(res.status_code) #it will print status code of given resopnse object
#this file contains enire Romeo Juliet play
print(len(res.text))  #will print the length of entire text
print(res.raise_for_status()) #it will create Exception for the failed download or false Download

 
#hellofile = open('rj.txt' , 'w') #opening file in write mode 
#hellofile.write(res.text) #writing all the data got from http://automatetheboringstuff.com/files/rj.txt to our file
#can be done in another way....
hellofile = open('rj.txt' , 'wb') #opening file in write in binary mode for preserving unicode 
for chunk in res.iter_content(123456):
	hellofile.write(chunk)
hellofile.close()

