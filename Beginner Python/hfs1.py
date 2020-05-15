#this is how python programs can run on Command Line

Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(5)
5
>>> print(10)
10
>>> progLanguages = ["Java", "C" , "C#" ,"C++"]
>>> progLanguages
['Java', 'C', 'C#', 'C++']
>>> print(progLanguages[1])
C
>>> print(len(progLanguages))
4
>>> progLanguages.append("php")
>>> progLanguages
['Java', 'C', 'C#', 'C++', 'php']
>>> progLanguages.pop()
'php'
>>> progLanguages.extend(["php","ruby","Go","R","Scala"])
>>> progLanguages.remove("rub")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    progLanguages.remove("rub")
ValueError: list.remove(x): x not in list
>>> progLanguages.remove("ruby")
>>> 

>>> 
>>> 
>>> progLanguages.insert(5,"javascript")
>>> progLanguages
['Java', 'C', 'C#', 'C++', 'php', 'javascript', 'Go', 'R', 'Scala']
>>> print(len(progLanguages))
9
>>> for(len(progLanguages)):
	
SyntaxError: invalid syntax
>>> progLanguages.insert(1,1)
>>> progLanguages.insert(3,3)
>>> progLanguages.insert(5,5)
>>> progLanguages.insert(7,7)
>>> progLanguages.remove(3,5,7)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    progLanguages.remove(3,5,7)
TypeError: remove() takes exactly one argument (3 given)
>>> progLanguages.remove(3)
>>> progLanguages.remove(5)
>>> progLanguages.remove(7)
>>> progLanguages.insert(3,2)
>>> progLanguages.insert(5,3)
>>> progLanguages.insert(7,4)
>>> progLanguages.insert(9,5)
>>> progLanguages.insert(11,6)
>>> progLanguages.insert(13,7)
>>> progLanguages.insert(15,8)
>>> progLanguages.insert(17,9)
>>> print(progLanguages)
['Java', 1, 'C', 2, 'C#', 3, 'C++', 4, 'php', 5, 'javascript', 6, 'Go', 7, 'R', 8, 'Scala', 9]
>>> for each_item in progLanguages:
	each_item=each_item+1
	progLanguages.remove(each_item)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    each_item=each_item+1
TypeError: can only concatenate str (not "int") to str
>>> for each_item in progLanguages:
	each_item=each_item++
	progLanguages.remove(each_item)
	
SyntaxError: invalid syntax
>>> j%1
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    j%1
NameError: name 'j' is not defined
>>> for each_item in progLanguages:
	print(each_item)

	
Java
1
C
2
C#
3
C++
4
php
5
javascript
6
Go
7
R
8
Scala
9
>>> count=0
>>> while count=len(progLanguages):
	
SyntaxError: invalid syntax
>>> count=1
>>> while count==len(progLanguages):
	progLanguages.remove(progLanguages[count])
	count=count+2

	
>>> for each_item in progLanguages:
	print(each_item)

	
Java
1
C
2
C#
3
C++
4
php
5
javascript
6
Go
7
R
8
Scala
9
>>> while count==len(progLanguages):
	progLanguages.remove(progLanguages[count])
	count=count+2

	
>>> progLanguages
['Java', 1, 'C', 2, 'C#', 3, 'C++', 4, 'php', 5, 'javascript', 6, 'Go', 7, 'R', 8, 'Scala', 9]
>>> 
