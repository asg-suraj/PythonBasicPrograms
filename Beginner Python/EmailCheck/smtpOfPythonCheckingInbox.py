import imapclient

conn=imapclient.IMAPClient('imap.yopmail.com', ssl=True)
conn.login('pi@yopmail.com','PleaseTypePasswordOfTheMail')
print(conn.select_folder('INBOX',readonly=True))
UIDs=conn.search(['SINCE 20-Mar-2017'])
print(UIDs)
#please see documentaion or automate the boring stuff with python not working program here 
