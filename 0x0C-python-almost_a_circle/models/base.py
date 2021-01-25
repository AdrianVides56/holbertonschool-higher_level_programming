#!/usr/bin/python3
""" Initializes module """
import json


class Base:
    """ Initializes class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        list_dict = []
        if list_objs is None:
            list_objs = []
        for a in list_objs:
            list_dict.append(cls.to_dictionary(a))
        with open(("{}.json".format(cls.__name__)), 'w') as my_file:
            my_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        list_return = []
        json_list = []
        try:
            with open(("{}.json".format(cls.__name__))) as my_file:
                json_list = cls.from_json_string(my_file.read())
        except FileNotFoundError:
            return json_list

        for a in json_list:
            list_return.append(cls.create(**a))

        return list_return
