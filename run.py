from flask import Flask,make_response
from app.libs.helper import  is_isbn_or_key

app = Flask(__name__)

@app.route("/book/search")
def search():
    form = request.args().todict()
    print(form)
    # isbn_or_key = is_isbn_or_key(q)
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=5000)
