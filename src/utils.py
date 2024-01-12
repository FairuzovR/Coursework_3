import os
import json
from class_file import Transactiondata


def displays_list():
    """открывает файл с данными и выводит список операций"""
    root_path = os.path.dirname(__file__)
    with open(os.path.join(root_path, '../operations.json')) as file:
        raw_json = file.read()
        operations_file = json.loads(raw_json)

    return operations_file


def filter_list():
    """Фильтрует лист по результату операции EXECUT и выдает список последних 5-ти операций"""
    operations_list = list()
    keys = ("id", "date_", "state", "operationAmount", "description", "from", "to")
    for item in displays_list():
        if set(keys).issubset(item):
            operations_list.append(item)
    del operations_list[0:len(operations_list) - 5]

    return operations_list


#  print(filter_list()

def creates_instance():
    """Создает экземпляры - 5 шт"""
    instance = list()
    for item in filter_list():
        instance.append([Transactiondata(item["id"], item["date_"], item["state"], item["operationAmount"],
                                         item["description"], item["from"], item["to"])])

    return instance

