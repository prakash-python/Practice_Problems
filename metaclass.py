class mymeta(type):
    def __new__(cls,name):
        print(cls.name)
        return super().__new__(cls,name)
class myclass(metaclass=mymeta):
    pass
