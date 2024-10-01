import uuid

class Url:
    
    def __init__(self):
        self.source: str= None
        self.url: str = None
        self.search_keyword: str = None
    
    def set_source(self, source):
        self.source = source
        
    def set_url(self, url):
        self.url = url
        
    def set_search_keyword(self, search_keyword):
        self.search_keyword = search_keyword
        
class Content:
    def __init__(self, text, url):
        self.text: str = text
        self.url: Url = url
