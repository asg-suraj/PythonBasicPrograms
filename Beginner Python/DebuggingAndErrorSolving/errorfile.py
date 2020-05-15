#we will write error in errorfile
import traceback

try:
	raise Exception('This is an Exception Example error message generated due to errorfile.py')
except:
	errorfile = open('errorfile.txt','a')
	errorfile.write(traceback.format_exc())
	errorfile.close()
	print('The Traceback info is written in errorfile.txt')

	
