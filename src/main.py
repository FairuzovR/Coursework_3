from utils import creates_instance

for item in creates_instance():
    print(f'{item.data_operation()} {item.status_description()}\n'
          f'{item.sent_from()}{item.sent_to()}\n'
          f'{item.displays_amount()} {item.displays_currency()}\n')
