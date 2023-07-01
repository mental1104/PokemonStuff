'''
Date: 2023-06-29 23:18:12
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 17:25:26
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base
from schema.pokemon import PokemonTuple
from sqlalchemy.exc import IntegrityError

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    HP = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    special_attack = Column(Integer)  
    special_defense = Column(Integer)  
    speed = Column(Integer)  
    type1 = Column(Integer, ForeignKey('type.id'))
    type2 = Column(Integer, ForeignKey('type.id'), nullable=True)
    ability1 = Column(Integer, ForeignKey('ability.id'))
    ability2 = Column(Integer, ForeignKey('ability.id'), nullable=True)
    hidden_ability = Column(Integer, ForeignKey('ability.id'), nullable=True)

    @staticmethod
    def create(session, input: PokemonTuple):
        record = Pokemon(**input.dict())
        try:
            session.add(record)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            print(record.name)
            print(e)
            # print(f"存在重复主键 {e}")
        return record.id
    

