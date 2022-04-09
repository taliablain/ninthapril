from application import db

from application.models.books import BOOK_INFO
from application.models.loans import LOAN_LOG
from application.models.users import USER_INFO

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/Exercise18', echo=False)
Session = sessionmaker(bind=engine)

session = Session()

book = session.query(BOOK_INFO).filter_by(BOOK_ID=1).first()
print(book.TITLE)

user = session.query(USER_INFO).filter_by(ID=1).first()
print(user.LASTNAME, user.FIRSTNAME, user.EMAIL)

loans = session.query(LOAN_LOG).filter_by(CUST_ID=1).first()
print(loans.BOOK_ID)
#for book in loans.BOOK_ID:
    #print(book.TITLE)



