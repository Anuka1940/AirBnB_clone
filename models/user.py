#!/usr/bin/python3
'''Model that inhererits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class that inherits from BaseModel'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
