from datetime import datetime

class Transactiondata:

    def __init__(self, id_, date_, state, operationamount, description, from_, to):
        #  id_ – id транзакциии
        #  date – информация о дате совершения операции
        #  state – статус перевода (EXECUTED или CANCELED)
        #  operationamount – сумма операции и валюта
        #  description – описание типа перевода
        #  from_ - откуда (может отсуствовать)
        #  to - куда
        self.id_ = id_
        self.date_ = date_
        self.state = state
        self.operationamount = operationamount
        self.description = description
        self.from_ = from_
        self.to = to

    def data_operation(self):
        thedate_one = datetime.strptime(self.date_, "%Y-%m-%dT%H:%M:%S.%f")
        return print(thedate_one.strftime("%d.%m.%Y"))


    def status_description(self):
        return print(self.description)


    def sent_from(self):
        pass


a = Transactiondata('1', "2018-06-08T16:14:59.936274", '1', '1', '2', '1', '1',)
a.data_operation()
a.status_description()

