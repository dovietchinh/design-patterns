from typing import Any


class Registry(type):
    _Registry = {}
    def __new__(cls,name,bases,atts):
        cls._Registry[name] = cls
        print('name: ',name)
        print('bases: ',bases)
        print('atts: ',atts)
        # print('cls: ',cls)
        # new_cls = type.__new__(cls,name,bases,atts)
        return type.__new__(cls,name,bases,atts)
    
    # def __init__(self):
    #     print('self')
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)

    @classmethod
    def get_registry(cls):
        return cls._Registry


class parent1():
    def asd(self):
        print('asd')

class abc(parent1,metaclass=Registry):
    pass
    # def __init__(self,a):
    #     print('this is abc class')
        # self.a = a

class abcd(metaclass=Registry):
    def __init__(self,a):
        print('this is abcd class')
        self.a = a
    
class parent2(type):
    def __new__(*args,**kwargs):
        print('parent3')
        print(*args,**kwargs)
        return type.__new__(*args,**kwargs)
class abcde(metaclass=parent2):
    def __new__(*args,**kwargs):
        print('abcde')
        return super().__new__(*args,**kwargs)

# r = Registry.get_registry()
# a = r['abc'](4)

    
