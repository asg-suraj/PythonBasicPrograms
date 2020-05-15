import re
# \d = digit (0-9)
# \D = non digit
# \w = any letter,digit,underscore 
# \W = not \w
# \s = space, tab, newline



lyrics = ''' Robocop food eats 4 calling birds, 5 gold rings, 6 geese a-laying, 7 swans a-swimming, 8 maids a-milking, 9 ladies dancing, 10 lords a-leaping, 11 pipers piping, 12 drummers drumming, 3 French hens, 2 turtle doves, And 1 partridge in a pear tree.'''
xmasRegex=re.compile(r'\d+ \w+') # + indicates one or more
print(xmasRegex.findall(lyrics))

#vowel recoginization
vowelRegex=re.compile(r'[aeiouAEIOU]')
mo=vowelRegex.findall(lyrics)
print(mo) #will print all vowels

doublevowelRegex =re.compile(r'[aeiouAEIOU]{2}')
mo=doublevowelRegex.findall(lyrics)
print(mo) #will print all vowels which comes 2 times side by side


#consonant recoginization
vowelRegex=re.compile(r'[^aeiouAEIOU]') # ^ will represent not symbol i.e not vowels is consonant
mo=vowelRegex.findall(lyrics)
print(mo) #will print all consonant
