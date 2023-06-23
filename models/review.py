#!/usr/bin/python3
''' Representation of a class Review that inherit from BaseModel'''
from models.base_model import BaseModel

class Review(BaseModel):
    '''Representation of Review'''
    plece_id = ''
    user_id = ''
    text = ''
