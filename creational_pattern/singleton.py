

class singleton:
    def __init__(self,cls):
        print('init')
        self._cls = cls
        self._instance = None

    def __call__(self,*args,**kwargs):
        print('args: ',args)
        print('kwargs: ',kwargs)
        if not self._instance:
            self._instance = self._cls(*args,**kwargs)
        return self._instance

@singleton
class Number:
    def __init__(self,number):
        print(f'class Number init with number={number}')
        self.number = number

    def action(self):
        self.number += 1

    def __repr__(self) -> str:
        return str(self.number)

@singleton
class Song:
    def __init__(self,name):
        print(f'class Song init with name={name}')
        self.name = name
       
    def action(self):
        self.name += " has been updated!"

    def __repr__(self) -> str:
        return self.name

print(Number._cls)
print(Number._instance)
first_number = Number(1)
print(Number._cls)
print(Number._instance)
first_number.action()
print("first_number: ",first_number)
second_number = Number(10)
print("second_number: ",second_number)

first_song = Song("Ngày mai em lấy chồng")
first_song.action()
print("first_song: ",first_song)
second_song = Song("Ngày mai em không lấy chồng nữa")
print("second_song: ",second_song)




# class SingletonMeta(type):
#     def __init__(self, *args, **kwargs):
#         self._instance = None
#         super(SingletonMeta, self).__init__(*args, **kwargs)

#     # def __new__(cls,name,bases,atts):
#     #     print('name: ',name)
#     #     print('bases: ',bases)
#     #     print('atts: ',atts)
#     #     return super(SingletonMeta,cls).__new__(cls,name,bases,atts)

#     def __call__(self, *args, **kwargs):
#         if not self._instance:
#             self._instance = super(SingletonMeta, self).__call__(*args, **kwargs)
#         return self._instance

class AS():
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print('init subclass AS')
    def asd(self):
        print('AS')


class chinhdv(AS):
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print('init subclass chinhdv')
    def asd(self):
        print('AS')


class chinhdv2(AS):
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print('init subclass chinhdv2')
    def asd(self):
        print('AS')
    

# class Person(chinhdv,chinhdv2,metaclass=SingletonMeta):

#     def __init__(self,age,asd=None):
#         self.name = 'kiennt'
#         self.age = age

#     def __new__(cls,*args,**kwargs):
#         return super(Person, cls).__new__(cls)

#     def asd():
#         super(Person,type).asd()
# # print(Person.mro())
# # 


# a = Person(4,20)
# # print(a.name) # kiennt 
# # print(a.age) # 26
# # b = Person(5)
# # print(b == a) # True
# # print(b.age)

