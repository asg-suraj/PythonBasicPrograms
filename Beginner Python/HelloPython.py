#This Program Says my Name for Sake of First Program and this is Comment

print('Hello World')
print('What is your name') #ask for name
myname= input() #took input name

print('your name is '+ myname)
print('The length of my name is ')
print(len(myname))   #length of String

print('what is your age') #ask for age
age = input()

print('you will be ' + str(int(age)+1) + ' in a year')  #typeCast int to String

#functions By Own

def firstFunction():
    print("Hello  Sun" , end='') # Default newline charachter avoided 
    print("Your Address is MAIT")
    print("your Number is 161321")

firstFunction()
firstFunction()

def plusOne(number):
    return number+1

print('The Number after adding one in 6 is ' + str(plusOne(6)))

print('Ram' , 'Sham' , 'Dhyan')

print('Ram' , 'Sham' , 'Dhyan' , sep='SPACE') #word SPACE will come between each word 

pine=1
pine = pine+1;
pine +=1 #both this and above same


print ('The indentation doesn\'t cause matter' + \
        'it will not take it')
