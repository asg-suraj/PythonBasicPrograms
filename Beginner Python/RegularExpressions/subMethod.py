import re

namesRegex = re.compile(r'Agent \w+',re.I)
mo=namesRegex.findall('Agent nana gives imp Docs to agent Chinya ')
print(mo) #will print Agent names
#but Agent Names Must be kept secret so what we do is
mo=namesRegex.sub('secretAgent','Agent nana gives imp Docs to agent Chinya ') #sub method substite whatever wanted to replace
print(mo) 

namesSecretRegex=re.compile(r'Agent (\w)\w*',re.I)
phrase='Agent nana gives imp Docs to agent Chinya '
#mo=namesSecretRegex.findall(phrase)
phrase=namesSecretRegex.sub(r'Agent \1****',phrase)
print(phrase)

