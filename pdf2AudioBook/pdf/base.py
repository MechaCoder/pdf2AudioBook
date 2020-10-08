from PyPDF2 import PdfFileReader

def makeReaderObject(path:str):
    return PdfFileReader(
        open(path, 'rb')
    )
