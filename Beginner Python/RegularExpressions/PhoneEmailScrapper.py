#! python3
import re
import pyperclip
#ToDo: Create a regex for phone numbers
phoneNumberRegex=re.compile(r'\d{3}-\d{3}-\d{4}') #another regex can be '\d{10}' or r'(\+\d\d)\d{10}' and So on

#
#ToDo: Create a regex for email address
#emailRegex=re.compile(r'\w+@\w+\.\w+') #This can be one regex
#print(emailRegex.search('my email id is srj5509@gmail.com'))
emailRegex =re.compile(r''' 
	# #something@something.something
	[a-zA-z0-9_.+]+  #name part
	@				# @ symbol
	[a-zA-z0-9_.+]+ #lastpart
	''',re.VERBOSE )



text=pyperclip.paste()
#select whatever document text and copy all to clipbord and then run the code

mophone=phoneNumberRegex.findall(text)
print('phone Numbers in the copied text')
if mophone!=None:
	for i in mophone:
		print(i+' ,')
else:
	print(mophone)

moEmail=emailRegex.findall(text)
print('email id\'s in the copied text')
if moEmail!=None:
	for i in moEmail:
		print(i+' ,')
else:
	print(moEmail)


#copy all extracted phoneNumbers and Email Id's on Clipboard
results= '\n'.join(mophone)+ '\n'+'\n'.join(moEmail)
pyperclip.copy(results) #will copy all results on clipboard
