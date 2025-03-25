import logging


class SimpleMeta(type):

    def __new__(cls, name, bases, namespace):
        # new_class = super().__new__(cls, name, bases, namespace)  # 1 var
        new_class = type(name, bases, namespace)  # 2 var
        print(namespace['full_name'])
        return new_class


class SimpleClass(metaclass=SimpleMeta):
    var = 3
    full_name = 'Bred Thomas'

    def __init__(self):
        self.bom = 13
        self.dom = 'something'

    def some_func(self):
        return 'do something'

    def some_func_with_arg(self, arg):
        return f'do something with {arg}'


clazz = SimpleClass()
