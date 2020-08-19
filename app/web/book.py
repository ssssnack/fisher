from flask import request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


# @app.route("/book/search")
# def search():
#     form = request.args.to_dict()
#     print(form)
#     isbn_or_key = is_isbn_or_key(form['q'])
#     yushu_book = YuShuBook()
#     if isbn_or_key == 'isbn':
#         res = yushu_book.search_by_isbn(form['q'])
#     else:
#         res = yushu_book.search_by_keyword(form['q'])
#     print(res)
#     return res