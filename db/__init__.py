'''
Date: 2023-07-01 11:13:17
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 17:29:40
'''

import os
import logging

from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


_Session = sessionmaker()

Base = declarative_base()

@contextmanager
def open_session():
    session = _Session()

    try:
        yield session
        session.commit()
    except Exception:
        logging.info("Something wrong")
        session.rollback()
        raise
    finally:
        session.close()

def get_pg_url():
    db_password = os.environ.get('DB_PASSWORD')
    ip = "localhost"
    port = 5432
    database = "pokemon"
    db_url = f"postgresql://postgres:{db_password}@{ip}:{port}/{database}"
    return db_url

def startup():
    url = get_pg_url()
    engine = create_engine(
        url,
        pool_pre_ping=True,
        pool_size=20,
        pool_recycle=3600
    )
    
    _Session.configure(bind=engine)

    Base.metadata.create_all(bind=engine)
    