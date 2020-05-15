import smtplib

conn = smtplib.SMTP('smtp.outlook.com',587) #smtp server and port Number

print(type(conn))
print(conn)
conn.ehlo() #to check and start connection
conn.starttls() #tls to send password over Encryption
conn.login('shrui@yopmail.com','PasswordOfThisMail')
conn.sendmail('shrui@outlook.com','Reciver@gmail.com','Subject: Mail Sent remotely.. \n\n Dear Shrui \n   So long to see you buddy this mail is created and sent through one python program using smtplib module from outlook as gmail do not support this  so used outlook now...... \n Love Suraj') #the first 2 '\n' after subject are quite important

conn.quit()