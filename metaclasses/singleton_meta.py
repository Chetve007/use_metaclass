
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Example with call"""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass
