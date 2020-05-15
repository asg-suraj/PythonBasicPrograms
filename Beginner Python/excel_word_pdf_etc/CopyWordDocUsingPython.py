import docx

def getText(filename):
	doc=docx.Document(filename)
	fullText=[]
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)


#here you can also use pyperclip model to copy all content to clipboard

print(getText('wordByPython.docx'))