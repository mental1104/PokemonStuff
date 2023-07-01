'''
Date: 2023-07-01 13:06:13
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 16:29:36
'''
from sqlalchemy import Column, Integer, String, ARRAY
from db import Base
from schema.type import TypeTuple
from sqlalchemy.exc import IntegrityError

class Type(Base):
    __tablename__ = 'type'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    zero = Column(ARRAY(Integer))
    low = Column(ARRAY(Integer))
    medium = Column(ARRAY(Integer))
    high = Column(ARRAY(Integer))

    @staticmethod
    def create(session, input: TypeTuple):
        record = Type(**input.dict())
        try:
            session.add(record)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            # print(f"存在重复主键 {e}")
        
        return record.id