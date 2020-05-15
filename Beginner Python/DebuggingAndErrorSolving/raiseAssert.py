

def drawBox(symbol,height,width):
	if len(symbol)!=1:
		raise Exception ("symbol needs to a string of length 1") #raised Our own message in Exception
	if width<=1 or height <=1:
		raise Exception ("height and width must be greater than 1")

	print(symbol * width)
	for i in range(0,height-2):
		print(symbol+' ' * (width-2)+symbol)
	print(symbol * width)

drawBox('*',5,15)