#!/usr/bin/env python3
"""The file_storage module that contains the FileStorage class."""

import json
from models.base_model import BaseModel
from models.classes import classes


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key, obj in self.__objects.items():
            json_obj[key] = obj.to_dict(save_to_disk=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key, value in json_obj.items():
                class_name = key.split('.')[0]
                self.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload method for deserializing the JSON file to objects"""
        self.reload()
