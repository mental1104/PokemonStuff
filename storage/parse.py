'''
Date: 2023-07-01 12:30:22
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 17:27:50
'''

import csv
import copy
from db import open_session
from schema.nature import NatureTuple
from model.nature import Nature
from schema.ability import AbilityTuple
from model.ability import Ability
from schema.type import TypeTuple
from model.type import Type
from schema.pokemon import PokemonTuple
from model.pokemon import Pokemon

class ParseData:
    
    
    @staticmethod
    def parse_nature():
        with open('/home/espeon/Pokemon/storage/data/natures.csv', 'r') as f:
            reader = csv.reader(f)
            
            next(reader)

            with open_session() as session:
                for row in reader:
                    record = NatureTuple(
                        id=row[0],
                        name=row[1],
                        decreased_stat=row[2],
                        increased_stat=row[3]
                    )
                    Nature.create(session, record)
    
    
    @staticmethod 
    def parse_ability():
        with open('/home/espeon/Pokemon/storage/data/abilities.csv', 'r') as f:   
            reader = csv.reader(f)
            
            next(reader)

            with open_session() as session:     
                for row in reader:
                    record = AbilityTuple(
                        id=row[0],
                        name=row[1]
                    )
                    Ability.create(session, record)        
            
    
    @staticmethod
    def parse_type():
        name_mapping = {}
        stat_mapping = {}
        
        with open('/home/espeon/Pokemon/storage/data/types.csv', 'r') as types:  
            reader = csv.reader(types)
            next(reader)
            for row in reader:
                type_id = int(row[0])
                name_mapping[type_id] = row[1]
        
   
        with open('/home/espeon/Pokemon/storage/data/type_efficacy.csv', 'r') as efficacy:
            reader = csv.reader(efficacy)
            next(reader)
            id = -1
            group = {}
            for row in reader:
                damage_type_id = int(row[0])
                target_type_id = int(row[1])
                damage_factor = int(row[2])
                
                if id != damage_type_id:
                    if id != -1:
                        stat_mapping[id] = copy.deepcopy(group)
                        
                    id = damage_type_id
                    group = {}
                    group["zero"] = []
                    group["low"] = []
                    group["medium"] = []
                    group["high"] = []
                

                if damage_factor == 0:
                    group["zero"].append(target_type_id)
                elif damage_factor == 50:
                    group["low"].append(target_type_id)
                elif damage_factor == 100:
                    group["medium"].append(target_type_id)
                elif damage_factor == 200:
                    group["high"].append(target_type_id)
                    
                if id > 17:
                    stat_mapping[id] = copy.deepcopy(group)
                    
                    
                    
        with open_session() as session:
            for type_id, value in stat_mapping.items():
                # 获取名字
                name = name_mapping[type_id]
                # 获取克制关系
                zero_list = value["zero"]
                low_list = value["low"]
                medium_list = value["medium"]
                high_list = value["high"]
                
                record = TypeTuple(
                    id=type_id,
                    name=name,
                    zero=zero_list,
                    low=low_list,
                    medium=medium_list,
                    high=high_list
                )
                
                Type.create(session, record)
    
    
    @staticmethod
    def parse_pokemon():
        name_mapping = {}
        type_mapping = {}
        ability_mapping = {}
        stat_mapping = {}
        
        with open('/home/espeon/Pokemon/storage/data/pokemon.csv', 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            for row in reader:
                id = int(row[0])
                name = row[1]
                name_mapping[id] = name
                     
                     
        with open('/home/espeon/Pokemon/storage/data/pokemon_types.csv', 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            
            id = -1
            group = {}
            for row in reader:
                pokemon_id = int(row[0])
                type_id = int(row[1])
                slot_id = int(row[2])
                
                if id != pokemon_id:
                    if id != -1:
                        type_mapping[id] = copy.deepcopy(group)
                
                    id = pokemon_id
                    group = {}
                    
                if slot_id == 1:
                    group["type1"] = type_id
                elif slot_id == 2:
                    group["type2"] = type_id
                
                if id == list(name_mapping)[-1]:
                    type_mapping[id] = copy.deepcopy(group)
                    
                    
        # 解析能力
        with open('/home/espeon/Pokemon/storage/data/pokemon_abilities.csv', 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            
            id = -1
            group = {}
            
            for row in reader:
                pokemon_id = int(row[0])
                ability_id = int(row[1])
                is_hidden = int(row[2])
                slot_id = int(row[3])
                if id != pokemon_id:
                    if id != -1:
                        ability_mapping[id] = copy.deepcopy(group)
                        
                    id = pokemon_id
                    group = {}
                    
                if is_hidden == 1:
                    group["hidden_ability"] = ability_id
                    continue
                
                if slot_id == 1:
                    group["ability1"] = ability_id
                elif slot_id == 2:
                    group["ability2"] = ability_id
                
                if id == list(name_mapping)[-1]:
                    ability_mapping[id] = copy.deepcopy(group)
                    
                
                
        # 解析种族值
        with open('/home/espeon/Pokemon/storage/data/pokemon_stats.csv', 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            
            id = -1
            group = {}
            for row in reader:
                
                
                pokemon_id = int(row[0])
                stat_id = int(row[1])
                base_stat = int(row[2])
                
                if id != pokemon_id:
                    if id != -1:
                        stat_mapping[id] = copy.deepcopy(group)
                    
                    id = pokemon_id
                    group = {}
                
                if stat_id == 1:
                    group["HP"] = base_stat
                elif stat_id == 2:
                    group["attack"] = base_stat
                elif stat_id == 3:
                    group["defense"] = base_stat
                elif stat_id == 4:
                    group["speAttack"] = base_stat
                elif stat_id == 5:
                    group["speDefense"] = base_stat
                elif stat_id == 6:
                    group["speed"] = base_stat
                
                if id == list(name_mapping)[-1]:
                    stat_mapping[id] = copy.deepcopy(group)
                    
                
                
        with open_session() as session:
            for pokemon_id in name_mapping.keys():
                name = name_mapping[pokemon_id]
                hp = stat_mapping[pokemon_id]["HP"]
    
                attack = stat_mapping[pokemon_id]["attack"]
                defense = stat_mapping[pokemon_id]["defense"]
                special_attack = stat_mapping[pokemon_id]["speAttack"]
                special_defense = stat_mapping[pokemon_id]["speDefense"]
                speed = stat_mapping[pokemon_id]["speed"]
                
                type1 = type_mapping[pokemon_id]["type1"]
                type2 = type_mapping[pokemon_id].get("type2")
                
                ability1 = ability_mapping[pokemon_id].get("ability1")
                ability2 = ability_mapping[pokemon_id].get("ability2")
                hidden_ability = ability_mapping[pokemon_id].get("hidden_ability")
                
                try:
                    record = PokemonTuple(
                        id=pokemon_id,
                        name=name,
                        HP=hp,
                        attack=attack,
                        defense=defense,
                        special_attack=special_attack,
                        special_defense=special_defense,
                        speed=speed,
                        type1=type1,
                        type2=type2,
                        ability1=ability1,
                        ability2=ability2,
                        hidden_ability=hidden_ability
                    )
                except:
                    print(record.name)
                    exit(1)
                
                Pokemon.create(session, record)


    @staticmethod
    def init():
        ParseData.parse_nature()
        ParseData.parse_ability()
        ParseData.parse_type()
        ParseData.parse_pokemon()