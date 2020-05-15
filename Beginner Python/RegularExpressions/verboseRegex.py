#for making long regex trick readable and if we don't care for whitespace character
import re 

verboseRegex = re.compile(r''' 
(\d\d\d #area code
-	   #first dash
\d\d\d  #first 3 digits
-      # Second dash
(\d\d\d)) #last digits
''' ,re.VERBOSE)
mo=verboseRegex.search('987-654-4321 is my number')
print(mo)
mo=verboseRegex.findall('987-654-4321 is my number')
print(mo)

verboseRegex = re.compile(r''' 
(\d\d\d-) | #area code
(\(\d\d\d\) )  #first 3 digits
\d\d\d
-      # Second dash
\d\d\d\d #last digits
\sx\d{2,4} #extensions like x1234 ''' ,re.VERBOSE |re.DOTALL | re.VERBOSE)
mo=verboseRegex.findall('987-654-4321 x1234 is my number')
print(mo)