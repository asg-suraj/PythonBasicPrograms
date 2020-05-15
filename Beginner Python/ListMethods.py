#List methods of python

#index of item
spam = ['kali','burp','metasploit','python','sqlmap','kali']
print(spam.index('kali')) #will show the index when it sees first time


#append
spam.append('gedit')


#insert
spam.insert(1, 'Linux') #inserts value at index 1 in spam
print(spam)

#remove

spam.remove('kali')  #will remove the value which it sees first time


#sort but it should have items of same data types , it is sorted based on ASCII values
#means Capital letter comes before small letter
spam.sort

#for sorting in true alphabetical order
spam.sort(key=str.lower)
print(spam)

#when we assign one list to another variable we actually copy same list refrence on another variable
#so whatever changes that variable does on list will reflect on orignal


#but to create Exact copy Brand new seaprate list and not copying refrence we need to import copy package and use deepcopy method
#for that
import copy
copySpam = copy.deepcopy(spam)
