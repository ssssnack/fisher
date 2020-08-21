from app.libs.httper import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'
    isbn_douban_url ='https://api.douban.com/v2/book/isbn/{}?apikey=0df993c66c0c636e29ecbb5344252a4a'
    keyword_douban_url='https://api.douban.com/v2/book/search?apikey=0df993c66c0c636e29ecbb5344252a4a&q={}&count={}&start={}'
    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self,isbn):
        url = self.isbn_douban_url.format(isbn)
        result = HTTP.get(url)
        return result

    def search_by_keyword(self,keyword,page=1):
        url = self.keyword_douban_url.format(keyword,current_app.config['PER_PAGE'],
                                      self.calculate_start(page))
        result = HTTP.get(url)
        return result

    def calculate_start(self,page):
        return  (page - 1) * current_app.config['PER_PAGE']