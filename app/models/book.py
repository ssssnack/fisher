from mongoengine import *


class Book(Document):
    book_id = IntField(required=True,unique=True)
    title = StringField(required=True)
    author = StringField(default="未名", max_length=30)
    binding = StringField()
    publisher = StringField()
    price = StringField()
    pages = StringField()
    pubdate = StringField()
    isbn = StringField()
    summary = StringField()
    image = StringField()
    meta = { 'collection': 'book', 'strict': False}

