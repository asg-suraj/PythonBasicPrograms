import PyPDF2,os
#it can only extract text from pdf and not other data
#and have limited set of actions


pdf1File = open('meetingminutes.pdf','rb') #open in read binary
reader1 = PyPDF2.PdfFileReader(pdf1File) #reading first pdf

pdf2File = open('meetingminutes2.pdf','rb') 
reader2 = PyPDF2.PdfFileReader(pdf2File)  #reading second pdf

writer = PyPDF2.PdfFileWriter()   #writer variable for the pdf which is created by python only

for page_num in range(reader1.numPages):  #going through each page
	page=reader1.getPage(page_num)      #getting page
	writer.addPage(page)				#writing to new pdf 

for page_num in range(reader2.numPages):  #taking second pdf's all pages
	page=reader2.getPage(page_num)      #getting each page 
	writer.addPage(page)  				#writing(appending) to the new(created) pdf

outputfile = open('CombinedPDFs.pdf','wb')  #write binary
writer.write(outputfile)
outputfile.close()
pdf1File.close()
pdf2File.close()







