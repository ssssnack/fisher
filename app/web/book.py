from flask import request,Blueprint
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web
from app.models.book import Book

@web.route("/book/search")
def search():
    form = SearchForm(request.args)
    yushu_book = YuShuBook()
    print(form)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = yushu_book.search_by_isbn(q)
        else:
            res = yushu_book.search_by_keyword(q,page)
    else:
        res= form.errors
        print("搜索关键字不符合要求")

    return res