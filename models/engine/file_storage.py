#!/usr/bin/python
''' Module to  serializes and deserializes instances to/from JSON file'''
import json
import os

class FileStorage:
    ''' Serializes and deserializes JSON objects'''
    # private class attributes
    __file_path = "file.json"
    __objects = {}
    models = ('BaseModel', 'Amenity', 'User', 'City', 'State', 'Place', 'Review')

    def __init__(self, *args,  **kwargs):
        '''Constructor for the class'''
        pass

    
    def all(self):
        '''Return dictionary __object__objects'''
        return self.__objects

    def new(self, obj):
        ''' method to set in __objects the with key <obj class name >.id'''
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to json'''
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        ''' Desializes JSON file to __objects'''
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                from models.base_model import BaseModel

                for key, value in serialized_objects.items():
                    print("{} {}".format(key, value))
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

    def get_instance(self, class_name, instance_id):
        '''Retrieve an instance based on the class name and instances'''
        for key, value in FileStorage.__objects.items():
            if class_name + '.' + instance_id == key:
                if instance_id == value.id:
                    return value
        else:
           return None
    
    def delete_by_id(self, class_name, instance_id):
        '''delete an instance from the database by id'''
        for key, value in FileStorage.__objects.items():
            if class_name + '.' + instance_id == key:
                if instance_id == value.id:
                    del FileStorage.__objects[key]
                    break
        self.save()
    
    def get_all(self, model=''):
        '''find all instances of a model or give model'''
        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        result = []
        for key, value in FileStorage.__objects.items():
            if key.startswith(model):
                result.append(str(value))
        return result
