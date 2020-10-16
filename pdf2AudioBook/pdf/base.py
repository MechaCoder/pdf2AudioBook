from PyPDF2 import PdfFileReader
import ebooklib
from ebooklib import epub

def makeReaderObject(path:str):
    return PdfFileReader(
        open(path, 'rb')
    )

def makeEpubReaderObject(path:str):
    return epub.read_epub(path)
