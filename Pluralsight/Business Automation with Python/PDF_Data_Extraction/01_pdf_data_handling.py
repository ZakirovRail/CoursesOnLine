# pip install PyPDF2

import PyPDF2

f = open('./foo.pdf', 'rb')
pdfr = PyPDF2.PdfFileReader(f)
pdfr.numPages  # returns number of pages
page = pdfr.getPage(0)  # retieves teh first page of pdf
txt = page.extractText()  #  extracts all text from the first page
f.close()






