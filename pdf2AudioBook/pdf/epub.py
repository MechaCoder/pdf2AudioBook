from re import sub

import ebooklib
from .base import makeEpubReaderObject

def processTitle(t:str):
    return t.split('.')[0]

class Epub:

    def __init__(self, path:str):
        self.path = path
        self.obj = makeEpubReaderObject(path)

    def getsDocTitle(self):
        """ returns a string of document title if the meta dose not exist then
        returns filename
        """
        if self.obj.title != '':
            return self.obj.title

        filename = self.path.split('/')[-1]
        filename = filename.split('.epub')
        return filename[0]

    def getText(self):

        obj = self.obj
        content = []
        for each in obj.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            c = {
                'title': processTitle(each.get_name()),
                'content': sub('<[^<]+?>', '', each.get_body_content().decode())
            }
            content.append(c)
        return content
