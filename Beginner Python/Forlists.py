#forLoops with Lists


#range is data type shows list with numbers from lower limit(default 0) to upper limit 
print(range(4))

#so in for loops we can use lists instead of range as

for i in [0,1,2,3,4]:
    print(i)

#we can also make it like below

p=list('singhisking')

for i in p:
    print(i)
    

#we can add step in range as

j=list(range(0,100,2)) #it will print all values from 0-100 with steps of 2
print(j)

#there is another way as seen

for i in range(len(p)):
    print('Index ' + str(i)+' in p list is '+str(p[i]))

#assignment ways for lists
m=[1,2,3]
size,color,disposition=m #assigns size =m[1]=1 , color =m[2]=2 and so on
print(size) #will print 1

#This also works
size,color,taste = 'loose' , 'black', 'yum'
print(size) #will print loose

#This can be used for swapping
size , color = color , size
print(size) #will print black and hence size swapped with color
