from click import secho, progressbar

from .pdf.pdf import PDF
from .sound.content import normalise
from .sound.mp3 import convertStringToMp3

def convert(path:str):
    """ converts file to a mp3 """
    p = PDF(path)
    secho('converting content', fg='yellow')
    content = normalise(p.getText())
    secho('creating mp3', fg='yellow')
    return convertStringToMp3(content, p.getsDocTitle())

def convertsToSiris(path:str):
    p = PDF(path)
    secho('converting content', fg='yellow')
    content = p.getListOfPages()
    files = []
    pageInt = 0
    with progressbar(content) as bar:
        for page in bar:
            files.append(
                convertStringToMp3(page, f'{p.getsDocTitle()}-{pageInt}')
            )
            pageInt += 1
    return files
