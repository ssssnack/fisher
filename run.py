from flask import Flask,make_response,request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
app = Flask(__name__)


@app.route("/book/search")
def search():
    form = request.args.to_dict()
    print(form)
    isbn_or_key = is_isbn_or_key(form['q'])
    yushu_book = YuShuBook()
    if isbn_or_key == 'isbn':
        res = yushu_book.search_by_isbn(form['q'])
    else:
        res = yushu_book.search_by_keyword(form['q'])
    print(res)
    return res




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=5000)
