import re

# ?  it represent Either there or not 
batRegex=re.compile(r'Bat(wo)?man') #whatever is part in brackket(wo) can appear 1 or 0 times only
mo=batRegex.search('this Batwoman is not a hero')
print(mo.group()) #will print Batwomen


mo=batRegex.search('this Batwowowowowoman is not a hero')
print(mo) #will print None

PhonNumRegex=re.compile(r'(\d\d\d\d-)?\d\d\d\d\d\d')
mo=PhonNumRegex.search('My phone Number is 901181 and the name is yedpat') #it will accept this also because of ? given 
if mo!=None:
	print(mo.group())
else:
	print(mo)

mo=PhonNumRegex.search('My phone Number is 8805-901181 and the name is yedpat will meet at say dinner?') #it will accept this also because of ? given 
if mo!=None:
	print(mo.group())
else:
	print(mo)

QuestionMarkRegex=re.compile(r'dinner\?') #here \ is escape Charachter for ? 
mo = QuestionMarkRegex.search('My phone Number is 8805-901181 and the name is yedpat will meet at say dinner?')
print(mo.group()) #it will print dinner?

# *   it is for zero or more
batRegex=re.compile(r'Bat(wo)*man') #whatever is part in brackket(wo) can appear 1 or 0 times only
mo=batRegex.search('this Batwoman is not a hero')
print(mo.group()) #will print Batwomen

mo=batRegex.search('this Batman is not a hero')
print(mo.group())

mo=batRegex.search('this Batwowowowowowoman is not a hero')
print(mo.group()) #it is because * allows us to repeat at any times

# +  	it is for one or more
batRegex=re.compile(r'Bat(wo)+man') #whatever is part in brackket(wo) can appear 1 or 0 times only
mo=batRegex.search('this Batwoman is not a hero')
print(mo.group()) 
mo=batRegex.search('this Batwowowowowowoman is not a hero')
print(mo.group()) #it is because + allows us to repeat at any times (just not zero Times)


regex= re.compile(r'\+\*\?') #Escape Charachter use

# specific Number of repettion

haregex = re.compile(r'(Ha){3}')
mo=haregex.search('he said HaHaHa')
print(mo)

specificrepeatRegex = re.compile(r'(Ha){3,5}') # The Ha can be Searched is Either 3 times or 4 times or 5 times due to {3,5}
mo=haregex.search('he said HaHaHaHa')
print(mo)
#note Can also put brackets like {3,},{,3}

digiregex = re.compile(r'(\d){3,5}')
mo=digiregex.search('1234567890')
print(mo) #it will print 12345 being 5 is maximum limit 
#python match with greedy method

digiregex = re.compile(r'(\d){3,5}?') # ? will make non Greedy match
mo=digiregex.search('1234567890')
print(mo) #will match by non greedy method and print 123 as 3 is min












