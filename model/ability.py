'''
Date: 2023-07-01 12:59:57
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 16:57:55
'''

from sqlalchemy import Column, Integer, String
from db import Base
from schema.ability import AbilityTuple
from sqlalchemy.exc import IntegrityError

class Ability(Base):
    __tablename__ = 'ability'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    @staticmethod
    def create(session, input: AbilityTuple):
        record = Ability(**input.dict())
        try:
            session.add(record)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            # print(f"存在重复主键 {e}")

        
        return record.id