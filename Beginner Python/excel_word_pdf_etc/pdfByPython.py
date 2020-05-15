import PyPDF2,os
#it can only extract text from pdf and not other data
#and have limited set of actions


pdfFile = open('meetingminutes.pdf','rb') #open in writing reading
reader=PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page =reader.getPage(1)
print(page.extractText())



for i in range(reader.numPages):
	print(reader.getPage(i).extractText()) #will print entire pdf file

