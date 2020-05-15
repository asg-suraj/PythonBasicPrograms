import re

BeginsWithHelloRegex = re.compile(r'^Hello')
mo= BeginsWithHelloRegex.search('Hello There')
mo2= BeginsWithHelloRegex.search('he Said "Hello"')
print(mo) #will print because mo starts with hello
print(mo2) # will print None because not begining with Hello 

EndsWithWorldRegex= re.compile(r'world$')
mo= EndsWithWorldRegex.search('Hello world')
mo2= EndsWithWorldRegex.search('Hello world shrui')
print(mo) # will print cause ends with world
print(mo2) # will print cause ends with shrui

allDigitRegex= re.compile(r'^\d+$')
mo=allDigitRegex.search('123456789')
mo2=allDigitRegex.search('12345678f')
print(mo) #print value
print(mo2) # print None

# . charachter means any charachter except newline see Example below

atRegex = re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on flat mat with bat.')
print(mo) #all words with 'at' at the End # note in word flat lat is only printed because there is only one Dot

#now to also include flat
atRegex = re.compile(r'.{1,2}at')
mo=atRegex.findall('The cat in the hat sat on flat mat with bat.')
print(mo) #now it will include flat also 


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Shrui Last Name: sernavarte'))


# dot all 
serve = ' Serve the public trust \nCorona Virus aalay China madhun \nRamdas Rocks all other Shocks'

dotStar=re.compile(r'.*')
mo = dotStar.search(serve)
print(mo) #it will print only first line 'Serve the public trust' and not a new line
#To Print Entire line

dotStar=re.compile(r'.*',re.DOTALL)
mo = dotStar.search(serve)
print(mo) #it will print first \n

vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE) # illustration of ignore case we can also use re.i instead of re.IGNORECASE
mo=vowelRegex.findall('Shrui yoU Are the best person In katta')
print(mo) #it will ignore capital or small and print all vowels




