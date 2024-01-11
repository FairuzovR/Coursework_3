import os
import json


def displays_list():
    '''Открывает файл с данными и выводит список операций'''
    ROOT_PATH = os.path.dirname(__file__)
    with open(os.path.join(ROOT_PATH, '../operations.json')) as file:
        raw_json = file.read()
        operations_file = json.loads(raw_json)
        return operations_file


print(displays_list()[1]['id'])
