#Lists is something like array in python
#list can contain mulitiple data type
#list can have same items mulitiple time
#defining lists
spam =['shri','Chinu', 'dhiru','pro','mad']
print(spam)  #typing this will print Entire list
print(spam[0]) # this will print value at index 0
#can write list like
n= [1,
    2,
    3,
    4]
# is same as n=[1,2,3,4]



#we can also have lists of list
ram=[[1,2,3,4,5],['shri','Chinu', 'dhiru','propoint','madpoint']]
print(ram[1][3]) # will print propoint
print(ram[0][4]) # will print 5
print(ram[-1][-3]) # will print value dhiru

#Fun Fact we can use above technique to find alphabet in list of strings
#suppose we want to find m of madhuri in spam
print(spam[4][0])

#can use in everywhere
print('The roll number of ' + spam[-1] + ' is ' + str(ram[0][4]))

#assigning and having multiple data type
spam[1]=48 #roll number of amigo  48
print(spam)

#length of list
print(len(ram))
print(len(spam))

#Slicing
print(spam[1:3]) #will take value from 1 to 2(will not include 3)
#also
spam[3:5]=[31,38]
print(spam)

#diffrent techniques
print(str(spam[:2])+' is Equal to' + str(spam[0:2])) #will automatically print items from begining
print(str(spam[2:])+' is Equal to' + str(spam[2:5])) #will automatically print items till end(here 5)

#Deleting value at Index in list

del spam[1]
print('after deleting 48 spam is'+ str(spam))

#string concatenation

ram = ram+spam
print(ram)
 

#list Function
p=list('suryaisking')
print('the Data type of string becomes '+ str(type(p)) )
print('\n' + str(p)) #will print list





#to Check whether value is in list or not
print('shri' in spam)
print('shr' in spam)
