from application import db
from dataclasses import dataclass

#@dataclass
class BOOK_INFO(db.Model):
    BOOK_ID: int
    TITLE: str
    AUTHOR: str
    GENRE: str

    BOOK_ID = db.Column(db.Integer, primary_key=True)
    TITLE = db.Column(db.String(20), nullable=False)
    AUTHOR = db.Column(db.String(20), nullable=False)
    GENRE = db.Column(db.String(10), nullable=False)


