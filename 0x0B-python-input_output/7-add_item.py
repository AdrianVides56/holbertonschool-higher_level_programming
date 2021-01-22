#!/usr/bin/python3
""" Initializes module and import"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
my_list = load_from_json_file('add_item.json')

for i in range(1, len(argv)):
    my_list.append(argv[i])

save_to_json_file(my_list, 'add_item.json')