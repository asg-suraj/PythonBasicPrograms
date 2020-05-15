#without using regex
def isPhoneNumber(text):
	if len(text)!=12: #12 because it also cover two dashes
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True


print(isPhoneNumber('798-851-1651'))
print(isPhoneNumber('hello')) #it is not phone number hence false


#doing some stuff
message = 'call me on 798-851-1651 or at 984-748-5677'
#getting phone Numbers from text
for i in range(len(message)):
	chunk=message[i:i+12]
	if isPhoneNumber(chunk):
		print('phone number found '+chunk)



#now we will short the same code by using Regular Expressions
#Same Code again just by Different Methods

import re

PhoneNumRegex =re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # \d is representing digits in regex
#we created the pattern object for Phone number
#now to search this pattern in Text
print(PhoneNumRegex.search(message)) #will print match object
#now to only get the number and not <re.Match object; span=(11, 23), match='770-981-1481'>
mo=PhoneNumRegex.search(message)#match object variable named mo
print(mo.group()) #it will print the result

#to find all sustrings 
mo=PhoneNumRegex.findall(message)
print(mo) #will print list of 2 Numbers

PhoneNumRegex =re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d)')  # (\d\d\d\d) is used to create groups
message= 'Indian numbers are representing 7790-844481 the codes can be found https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India#Telecom_circles'
mo=PhoneNumRegex.search(message)
print(mo.group()) #will print all groups as regex defined
print('The Numbers deciding ISP and state is '+mo.group(1)) #will hence print only first group
print('the Actual Number is '+mo.group(2))# will print second group

message= 'Indian numbers are representing (7790)-844481 the codes can be found https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India#Telecom_circles'
#now to chcek (7709)-811481 like phone Numbers
PhoneNumRegex =re.compile(r'\(\d\d\d\d\)-\d\d\d\d\d\d')  # (\d\d\d\d) is used to create groups
mo=PhoneNumRegex.search(message)
print(mo.group()) #this will print brackets

