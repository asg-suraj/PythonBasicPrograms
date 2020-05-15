#here we are checking Traffic Signal Conditions of 2 ligths at a time 
#and for cars not to be clashed we need to keep one of the two pairs as always red
#and to check this conditions we will use assert statement 
market_2nd = {'North-south':'green' , 'East-west':'red'}


def switchLights(intersection):
	for  key in intersection.keys():
		if intersection[key]=='green':
			intersection[key]='yellow'
		elif intersection[key]=='yellow':
			intersection[key]='red'
		elif intersection[key]=='red':
			intersection[key]='green'
	assert 'red' in intersection.values() , 'Neither light is red accident can happen  ' +str(intersection)
	#this assert system will check required Condition and will tell the Reason given


switchLights(market_2nd)

