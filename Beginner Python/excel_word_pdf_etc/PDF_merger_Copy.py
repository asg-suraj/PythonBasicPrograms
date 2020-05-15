import PyPDF2,os,sys
#it can only extract text from pdf and not other data
#and have limited set of actions
addresses=' '.join(sys.argv[1:]) #taking Cmd arguments and joining pdf's
print(addresses)
#if(addresses.__contains__('.pdf')):
pdfs=addresses.split()

print(pdfs)
writer = PyPDF2.PdfFileWriter()
for i in range(len(pdfs)-1):
	pdf1File = open(pdfs[i],'rb')
	reader1 = PyPDF2.PdfFileReader(pdf1File)
	pdf2File = open(pdfs[i+1],'rb')
	reader2 = PyPDF2.PdfFileReader(pdf2File)
	
	for page_num in range(reader1.numPages):  #going through each page
		page=reader1.getPage(page_num)      #getting page
		writer.addPage(page)
	for page_num in range(reader2.numPages):  #taking second pdf's all pages
		page=reader2.getPage(page_num)      #getting each page 
		writer.addPage(page)



outputfile = open('CombinedPDFs.pdf','wb')  #write binary
writer.write(outputfile)
outputfile.close()
pdf1File.close()
pdf2File.close()







