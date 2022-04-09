from application import db
from dataclasses import dataclass


#the annotation below will help to turn the Python object into a JSON object
@dataclass
class USER_INFO(db.Model):
    ID: int
    FIRSTNAME: str
    LASTNAME: str
    EMAIL: str
    ADDRESS: str
    POSTCODE: str

    ID = db.Column(db.Integer, primary_key=True)
    FIRSTNAME = db.Column(db.String(50), nullable=False)
    LASTNAME = db.Column(db.String(50), nullable=False)
    EMAIL = db.Column(db.String(50), nullable=False)
    ADDRESS = db.Column(db.String(50), nullable=False)
    POSTCODE = db.Column(db.String(10), nullable=False)


