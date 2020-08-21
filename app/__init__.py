from flask import Flask
from mongoengine import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    MONGODB_SETTING = app.config['MONGODB_SETTING']
    connect(MONGODB_SETTING['db'], host=MONGODB_SETTING['host'], port=MONGODB_SETTING['port'])
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)