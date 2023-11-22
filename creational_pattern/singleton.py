

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

