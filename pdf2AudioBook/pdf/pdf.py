from .base import makeReaderObject

class PDF:

    def __init__(self, path:str):
        self.path = path
        self.obj = makeReaderObject(path)

    def getsDocTitle(self):
        """ returns a string of document title if the meta dose not exist then
        returns filename
        """
        data = self.obj.getDocumentInfo()

        if '/Title' in data.keys() and data['/Title'] != '':
            return data['/Title']

        filename = self.path.split('/')[-1]
        filename = filename.split('.pdf')
        return filename[0]

    def getText(self):

        documentText = ""
        numPages = self.obj.numPages
        for pageId in range(0, numPages):
            documentText += self.obj.getPage(pageId).extractText()

        return documentText

    def getListOfPages(self):
        content = []
        numPages = self.obj.numPages
        for pageId in range(0, numPages):
            content.append(self.obj.getPage(pageId).extractText())

        return content
