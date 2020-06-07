from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, id: str, os: str, price: float):
        self.id = id
        self.os = os
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not value.isalpha() or len(value) < 8:
            raise Exception('Invalid id!')
        else:
            self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception('Invalid price!')
        else:
            self.__price = value

    def print_item(self):
        return f'Item id: {self.id}\nOperating system: {self.os}\nPrice: {self.price}'


class Phone(Item):
    @abstractmethod
    def __init__(self, id, os, price):
        Item.__init__(self, id, os, price)

    def make_call(self):
        print('Making call...')

    def receive_call(self):
        print('Receiving a call!')

    def send_message(self):
        print('Sending message...')

    def receive_message(self):
        print('Receiving a message!')


class Tablet(Item):
    def __init__(self, id, os, price):
        Item.__init__(self, id, os, price)

    def stream_movie(self):
        print('Streaming movie...')


class CellPhone(Phone):
    def __init__(self, id, os, price):
        Phone.__init__(self, id, os, price)


class SmartPhone(Phone):
    def __init__(self, id, os, price, apps: list):
        Phone.__init__(self, id, os, price)
        self.apps = apps

    def browse_internet(self):
        print('Browsing...')

    def print_item(self):
        return f'Item id: {self.id}\nOperating system: {self.os}\nPrice: {self.price}\nApplications: {", ".join(self.apps)}'

    @property
    def apps(self):
        return self.__apps

    @apps.setter
    def apps(self, value):
        if len(value) < 5:
            raise Exception('Invalid number of applications!')
        else:
            self.__apps = value


items_dict = {'SmartPhone': [], 'CellPhone': [], 'Tablet': []}


def test_item(command_list, items_dict):
    id = command_list[1]
    functionality = command_list[2]
    found = False
    for search_item in items_dict.values():
        for one_item in search_item:
            if id == one_item.id:
                if functionality in dir(one_item):
                    format = f'one_item.{functionality}()'
                    eval(format)
                    found = True
    if not found:
        print('Invalid request has been made!')


def report_item(command_list, items_dict):
    kind = command_list[1]
    if kind in items_dict.keys():
        for item in items_dict.get(kind):
            print(item.print_item())
    else:
        print('Invalid request has been made!')


while True:
    command = input()
    if command == 'end':
        break
    try:
        type = command.split('(')[0]
        new_obect = eval(command)
        items_dict.get(type).append(new_obect)
    except Exception as ex:
        print(ex)

while True:
    command_list = input().split()
    if command_list[0] == 'end':
        exit(0)
    if command_list[0] == 'test':
        test_item(command_list, items_dict)
    elif command_list[0] == 'report':
        report_item(command_list, items_dict)

        # or

from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, item_id: str, operating_system: str, price: float):
        self.item_id = item_id
        self.operating_system = operating_system
        self.price = price

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value: str):
        if value.isalpha() and len(value) >= 8:
            self.__item_id = value
        else:
            raise Exception('Invalid id!')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value > 0:
            self.__price = value
        else:
            raise Exception('Invalid price!')

    def __str__(self):
        return f'Item id: {self.item_id}\nOperating system: {self.operating_system}\nPrice: {self.price}'


class Phone(Item):
    @abstractmethod
    def __init__(self, item_id: str, operating_system: str, price: float):
        Item.__init__(self, item_id, operating_system, price)

    def make_call(self):
        return 'Making call...'

    def receive_call(self):
        return 'Receiving a call!'

    def send_message(self):
        return 'Sending message...'

    def receive_message(self):
        return 'Receiving a message!'


class Tablet(Item):
    def __init__(self, item_id: str, operating_system: str, price: float):
        Item.__init__(self, item_id, operating_system, price)

    def stream_movie(self):
        return 'Streaming movie...'


class CellPhone(Phone):
    def __init__(self, item_id: str, operating_system: str, price: float):
        Phone.__init__(self, item_id, operating_system, price)


class SmartPhone(Phone):
    def __init__(self, item_id: str, operating_system: str, price: float, app_list: list):
        Phone.__init__(self, item_id, operating_system, price)
        self.app_list = app_list

    @property
    def app_list(self):
        return self.__app_list

    @app_list.setter
    def app_list(self, value: list):
        if len(value) >= 5:
            self.__app_list = value
        else:
            raise Exception('Invalid number of applications!')

    def browse_internet(self):
        return 'Browsing...'

    def __str__(self):
        applications = ', '.join(self.app_list)
        return f'Item id: {self.item_id}\nOperating system: {self.operating_system}\n' \
               f'Price: {self.price}\nApplications: {applications}'


item_dict = {}
while True:
    tokens = input()
    if 'end' == tokens:
        break
    try:
        item = eval(tokens)
        idnt = tokens.split(', ')[0].split('(')[1].lstrip('"').rstrip('"')
        if not item_dict.get(idnt):
            item_dict[idnt] = item
    except Exception as exc:
        print(exc)

while True:
    tokens = input().split()
    if 'end' == tokens[0]:
        break
    elif 'test' == tokens[0]:
        idnt = tokens[1]
        if item_dict.get(idnt):
            item = item_dict.get(idnt)
            try:
                eval_str = f'print(item.{tokens[2]}())'
                eval(eval_str)
            except Exception:
                print('Invalid request has been made!')
        else:
            print('Invalid request has been made!')
    elif 'report' == tokens[0]:
        kind = tokens[1]
        kind_found = False
        for val in item_dict.values():
            if type(val).__name__ == kind:
                print(val)
                kind_found = True
        if not kind_found:
            print('Invalid request has been made!')

            # or


    techs = []

line = input()

while not line == 'end':
    line = line.split('(')
    type_of_tech = line[0]

    if not (type_of_tech == 'SmartPhone' or type_of_tech == 'Tablet' or type_of_tech == 'CellPhone'):
        print(f'Can\'t instantiate abstract class {type_of_tech} with abstract methods __init__')
        line = input()
        continue

    rest = line[1].split(')')
    rest_list = rest[0].split(',')
    id_ = rest_list[0].split('"')
    id_ = id_[1]

    if not id_.isalpha() or len(id_) < 8:
        print('Invalid id!')
        line = input()
        continue

    oper_sys = rest_list[1].split('"')
    oper_sys = oper_sys[1]
    price = int(rest_list[2])

    if not price > 0:
        print('Invalid price!')
        line = input()
        continue

    if type_of_tech == 'SmartPhone':
        app_list = rest_list[3:]
        if not len(app_list) >= 5:
            print('Invalid number of applications!')
            line = input()
            continue
        tech = {
            'type_tech': 'SmartPhone',
            'id_of_tech': id_,
            'operating system': oper_sys,
            'price': price,
            'apps': app_list
        }
    elif type_of_tech == 'CellPhone':
        tech = {
            'type_tech': 'CellPhone',
            'id_of_tech': id_,
            'operating system': oper_sys,
            'price': price,
        }
    elif type_of_tech == 'Tablet':
        tech = {
            'type_tech': 'Tablet',
            'id_of_tech': id_,
            'operating system': oper_sys,
            'price': price,
        }

    techs.append(tech)
    line = input()

line = input()

while not line == 'end':
    line = line.split()
    t_r = line[0]

    if t_r == 'test':
        test_id = line[1]
        functionality = line[2]
        found = False

        for el in techs:
            if el['id_of_tech'] == test_id:
                found = True
                error_ = True

                if el['type_tech'] == 'Tablet':
                    if not functionality == 'stream_movie':
                        print('Invalid request has been made!')
                    else:
                        print('Streaming movie...')
                elif el['type_tech'] == 'SmartPhone':
                    if functionality == 'make_call':
                        error_ = False
                        print('Making call...')

                    if functionality == 'receive_call':
                        error_ = False
                        print('Receiving a call!')

                    if functionality == 'send_message':
                        error_ = False
                        print('Sending message...')

                    if functionality == 'browse_internet':
                        error_ = False
                        print('Browsing...')

                    if functionality == 'receive_message':
                        error_ = False
                        print('Receiving a message!')

                    if error_:
                        print('Invalid request has been made!')
                elif el['type_tech'] == 'CellPhone':
                    if functionality == 'make_call':
                        error_ = False
                        print('Making call...')

                    if functionality == 'receive_call':
                        error_ = False
                        print('Receiving a call!')

                    if functionality == 'send_message':
                        error_ = False
                        print('Sending message...')

                    if functionality == 'receive_message':
                        error_ = False
                        print('Receiving a message!')

                    if error_:
                        print('Invalid request has been made!')
        if not found:
            print('Invalid request has been made!')

    elif t_r == 'report':
        kind = line[1]

        if not kind == 'SmartPhone':
            if not kind == 'Tablet':
                if not kind == 'CellPhone':
                    print('Invalid request has been made!')
                    line = input()
                    continue

        for tec in techs:
            if tec['type_tech'] == kind:
                print(
                    f"Item id: {tec['id_of_tech']}\nOperating system: {tec['operating system']}\nPrice: {tec['price']}")
                if kind == 'SmarthPhone':
                    print(f"Applications:{'app_list'}")
    line = input()



