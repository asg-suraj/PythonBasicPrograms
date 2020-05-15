import re

batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
print(mo.group()) #and this finds Letter Batmobile successfully
print(mo.group(1)) #will print mobile as the mobile of batmobile is found
mo=batRegex.search('Batmotorcycle lost a wheel')
print(mo) #will print None
#note here you cannot use mo.group() hence it will print Errors

