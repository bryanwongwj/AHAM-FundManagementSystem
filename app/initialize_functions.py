from flask import Flask
from app.modules.fund.route import fund_bp
from app.db.db import db
from flask_smorest import Api


def initialize_route(app: Flask):
    with app.app_context():
        api = Api(app)
        api.register_blueprint(fund_bp)

def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()