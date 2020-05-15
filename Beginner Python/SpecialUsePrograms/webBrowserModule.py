import webbrowser,sys,pyperclip

#webbrowser.open('http://playweb.eckovation.com/surajgurav/')  #it will open that website in Default browser
#we can try any website here example -https://www.google.com/

#now we will do some stuff
#we will create a script and will take address from one website and give that
#to maps.google.com to show the location in maps

sys.argv #['webBrowserModule.py' , '870' , 'Valencia' , 'st.']

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:]) #we did this because we take cmd arguments and do not want program name
else:
	address = pyperclip.paste()   #that means you have to copy the address on clipboard before executing the program

webbrowser.open('https://www.google.com/maps/place/'+address)