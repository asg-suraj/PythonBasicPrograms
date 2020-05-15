import re #python Lib for Regular Expression

print("Hello World")
print("Raja")
print("Hello:Nick".split(":"))
p = {"name": 'asgsrj', "college": "GCEK", "class": 'BE'}  # this is Dictionary

print(p)

print(p['name'])
str1 = "papa"
str2 = "nana"


def myprintingpress(str1, str2):
    print('This is my Function and HIII')
    print(str1 + " " + str2)


myprintingpress('ya', 'Bhau')

check = True

if (check == False):
    print("print this function")

elif (check == True):
    print("True answer")

else:
    print("Wrong Anser")

raja = " she said 'Ash is bad' ,But Madhu is 1234 good in Exams Too. ////" #escape Charachter for / is / only so for one / to print we need to write //

new1 = re.sub('[A-Z]', ' ', raja)  # removes Captial Words means Replacing space mentioned after Comma
print(new1)

new1 = re.sub('[a-z]', ' ', raja)  # removes small letter Words
print(new1)

new1 = re.sub('[.\',/]', ' ', raja)  # removes Mentioned punctuation marks
print(new1)


new1 =re.sub('[.\',/A-Za-z]',' ',raja)    #removes mentioned Charachter Words
print(new1)

new1 =re.sub('[.\',/A-Za-z0-9]',' ',raja)    #removes mentioned Charachters Words
print(new1)


