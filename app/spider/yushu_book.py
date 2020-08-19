

from app.libs.httper import HTTP

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    def search_by_keyword(self,keyword):
        count = 1
        start = 1
        url = self.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result