import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) #returns a list of all phone numbers

phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))') # has groups
mo=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # will print different type of o/p
# [('415', '555', '9999'), ('212', '555', '0000')] i.e with all groups

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-(\d\d\d\d)') # has groups then will print only groups of 4 as per groups detected
mo=phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)