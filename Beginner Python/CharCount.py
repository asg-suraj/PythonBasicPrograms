#will count charachter in string
import pprint
msg='Hi my name is sun and from San Fransico I like it here'

count={}

for charachter in msg.upper(): #will convert msg in upper case
    count.setdefault(charachter,0)
    count[charachter]=count[charachter]+1

pprint.pprint(count)
