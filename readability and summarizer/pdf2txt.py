import PyPDF2
def read_pdf(filename):
    #read the file:
    pdfFile = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdfFile)
    page_nos = pdf_reader.numPages
    #get all the pages:
    text = ""
    for page in range(page_nos):
        pages = pdf_reader.getPage(page)
        text += pages.extractText()
    new_file = open("data/txts/{}.txt".format(filename.strip("data/pdfs/").strip(".pdf")), "w")
    new_file.writelines(text)


if __name__ == "__main__":
    read_pdf("watchOS8.pdf")