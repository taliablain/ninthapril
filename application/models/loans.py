from application import db
from dataclasses import dataclass


class LOAN_LOG(db.Model):
    BOOK_ID: int
    CUST_ID: int
    DUE_DATE: str
    RETURNED: str

    BOOK_ID = db.Column(db.Integer, nullable=False)
    CUST_ID = db.Column(db.Integer, nullable=False)
    DUE_DATE = db.Column(db.String(20), primary_key=True)
    RETURNED = db.Column(db.String(3), nullable=False)
    #BOOK_ID = db.relationship('BOOK_INFO', backref='books')
    #CUST_ID = db.relationship('USER_INFO', backref='users')