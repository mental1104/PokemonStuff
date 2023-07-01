'''
Date: 2023-07-01 13:13:17
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 16:29:26
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from db import Base
from schema.nature import NatureTuple

class Nature(Base):
    __tablename__ = 'nature'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    decreased_stat = Column(Integer)
    increased_stat = Column(Integer)
    
    @staticmethod
    def create(session, input: NatureTuple):
        record = Nature(**input.dict())
        try:
            session.add(record)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            # print(f"存在重复主键 {e}")
        return record.id
    
    @classmethod
    def create_batch(cls, session, input: list[NatureTuple]):
        session.bulk_insert_mappings(cls, input)