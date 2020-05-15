str="That is Alice's is cat."
#use of Escape Charachter
str1='mom\'s food is best' # \ is Escape Charchter and hence it will ignore '
print(str,str1)
#also 
str2=' i can go\\went\\ to school'
# \\ means \
print(str2)
#MultiLine String
str3=''' hello My name Shyam Sundar and I want to talk 
about Our College 
I Study in MAIT and I 
Love Studying Computer hence I took IT Branch'''
print(str3)
print('The length of str3 is ')
print(len(str3))

spam='Hello World!'
print(spam.upper()) # spam is all shown in Capital 
print(spam.lower()) # spam is all shown in lower letters

#Example of Use
if spam.lower() == 'hello world!':
	print("Studied the Example")

#checking The things
print(spam.islower())
#will print False becuase not each Charachter is lowercase
print(spam.upper().isupper())
#this will return True because it is first Entirely converted to uppercase and then checked for uppercase letters
#the several other methods like
# isalpha() , isalnum(), isdecimal() , isspace() , istitle() ,etc

#startswith()
print(spam.startswith("Hello")) #will print True
print(spam.endswith("ld!"))#will print True

petnames=','.join(['cats','dogs','rabits']) #illustartion of join function
print(petnames)

petnames=' '.join(['cats','dogs','rabits']) #illustartion of join function with singlespace
print(petnames)

#now split function
words="I have some good Friends".split()
print(words) #will split with space


words1=' '.join(words)
words=words1.split('a') #will split with letter a
print(words)

#ljust() and rjust() are same with just Direction change
print(spam.rjust(15)) #will print after 15 spaces
#also
print(spam.ljust(28, '*'))
#Center
print(spam.center(20,' ')) #10 spaces on both sides
spam=spam.rjust(10)
#now to remove this Extra Whitespaces in any sides of spam we use
spam=spam.strip();
#we also have lstrip() and rstrip() 
print(spam)
print(spam.replace('l','_YXZ_')) #it will replace every l with _YXZ_

import pyperclip
pyperclip.copy('Hello!!!!!!!!')
#now this text is copied to the Clipboard and you can paste it anywhere

print(pyperclip.paste())
#Now it will paste whatever is in clipboard as String

name='Chaitnya'
place= 'Karad'
print(name +' come to the ' +place )#String Concatination

print("hello %s come to the %s" %(name,place))
#String Formatting


#in StringMethods.bat
#it will run program and will run default windows Pause program
#to try out you can type pause in cmd



