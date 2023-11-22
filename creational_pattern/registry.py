from typing import Any
class Registry():
    _Registry = {}    
    
    def __init__(self,cls):
        self._Registry[cls.__name__] = cls
        cls.get_registry = Registry.get_registry

    @classmethod
    def get_registry(cls):
        return cls._Registry
    
    @classmethod
    def get_member(cls,name):
        return cls._Registry[name]

@Registry
class Member1():
    def __init__(self):
        print("this is class member 1")

@Registry
class Member2():
    def __init__(self):
        print("this is class member 2")


print("Registry: ",Registry.get_registry())

a = Registry.get_member('Member2')()


