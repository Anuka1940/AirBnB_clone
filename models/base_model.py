#!/usr/bin/python3
'''A base Model for other project models'''
import uuid
from datetime import datetime

class BaseModel:
    '''Define all attributes and methods'''
    def __init__(self):
        '''Serialization or Deserialization'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        '''Override default __str__ method'''
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''Update updated_at with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''return a dict containing all keys/values of "__dict__"'''
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ['created_at','updated_at']:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
