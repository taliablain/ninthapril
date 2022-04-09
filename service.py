from application.models.users import USER_INFO
from application.models.books import BOOK_INFO
from application.models.loans import LOAN_LOG
from application import db


def get_all_books():

    return BOOK_INFO.query.all

def get_book_by_id(BOOK_ID):
    if BOOK_ID > 0:
        return BOOK_INFO.query.get(BOOK_ID)
    else:
        return None

def get_loans_by_id(CUST_ID):
    if CUST_ID < 10000:
        return LOAN_LOG.query.get(CUST_ID)
    else:
        return None
