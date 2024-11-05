class Url:
    
    def __init__(self):
        self.source: str= None
        self.url: str = None
        self.search_keyword: str = None
    
    def set_source(self, source):
        self.source = source
        return self
        
    def set_url(self, url):
        self.url = url
        return self
        
    def set_search_keyword(self, search_keyword):
        self.search_keyword = search_keyword
        return self
        
class Content:
    def __init__(self, text, search_keyword, url):
        self.text: str = text
        self.search_keyword: str = search_keyword
        self.url: str = url
