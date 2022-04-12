from application.models.users import USER_INFO
from application.models.books import BOOK_INFO
from application.models.loans import LOAN_LOG
from application import db


def get_all_books():
    books = db.session.query(BOOK_INFO)
    return BOOK_INFO.query.all()


def get_book_by_id(BOOK_ID):
    if BOOK_ID > 0:
        return BOOK_INFO.query.get(BOOK_ID)
    else:
        return None

def get_loans_by_id(CUST_ID):
    if CUST_ID < 10000:
        loans = db.session.query(LOAN_LOG).filter(LOAN_LOG.CUST_ID=='1').all()
        return loans
    else:
        return None

def get_books_on_loan():
    return LOAN_LOG.query.all()


print(get_loans_by_id(1))
