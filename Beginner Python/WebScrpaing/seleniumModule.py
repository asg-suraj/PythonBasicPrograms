from selenium import webdriver

browser = webdriver.Firefox() #will now open firefox

browser.get('https://automatetheboringstuff.com/')


#elem stores css selector object and the css selector is provided by us manually  just same as parsingHTMlwithBeautifulSoup.py 
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
print(elem)

elem.click() #it will simulate clicking on method (means here we have taken css selector of introduction on (automatetheboringstuff.com))

#to find all paragraphs and store in elems
elems=browser.find_elements_by_css_selector('p')
print(len(elems)) #will print length of list of paragraph


browser.get('https://www.google.com/')
#now we will try to type the things
searchelems=browser.find_element_by_css_selector('.gLFyf') #this is css selector for the field where we need to give input
searchelems.send_keys('Zophie') #here we simulate human typing with program typing
searchelems.submit() #this will be simulating pressing ok




#other browser features 
searchelems.back()
searchelems.forward()
searchelems.refresh()
searchelems.quit()  #will quit browser completly

print(searchelems.txt) #will get all string within selected css

#to get entire webpage browser.find_element_by_css_selector('html') can be used