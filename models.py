from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

DATABASE_NAME = "bookshelf"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "135792468"
DATABASE_PORT = "5432"
DATABASE_URL = "localhost"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
SQLALCHEMY_TRACK_MODIFICATIONS = "SQLALCHEMY_TRACK_MODIFICATIONS"

DATABASE_PATH = f"postgres://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config[SQLALCHEMY_DATABASE_URI] = DATABASE_PATH
    app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movie

'''


class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Integer)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'rating': self.rating,
        }
