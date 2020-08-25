import PyPDF2

pdf1 = open('./foo.pdf', 'rb')
pdf2 = open('./as.pdf', 'rb')

pdfr1 = PyPDF2.PdfFileReader(pdf1)
pdfr2 = PyPDF2.PdfFileReader(pdf2)
pdfw = PyPDF2.PdfFileWriter()

for pn in range(pdfr1.numPages):
    po = pdfr1.getPage(pn)
    pdfw.addPage(po)
for pn in range(pdfr2.numPages):
    po = pdfr2.getPage(pn)
    pdfw.addPage(po)
pdfo = open('./combined.pdf', 'wb')
pdfw.write(pdfo)

pdfo.close()
pdf1.close()
pdf2.close()
