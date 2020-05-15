from selenium import webdriver
import sys


item_to_search_list=sys.argv[1:]
item_to_search= ' '.join(item_to_search_list)
print('Searching for \''+item_to_search+'\' on google in firefox browser')
browser = webdriver.Firefox()
browser.get('https://www.google.com/')
#now we will try to type the things
searchelems=browser.find_element_by_css_selector('.gLFyf') #this is css selector for the field where we need to give input
searchelems.send_keys(item_to_search) #here we simulate human typing with program typing
searchelems.submit() #this will be simulating pressing ok