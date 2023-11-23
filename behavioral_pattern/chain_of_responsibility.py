from abc import ABCMeta, abstractmethod

class BaseHandler(metaclass=ABCMeta):
    def __init__(self):
        self._next = None
    
    def set_next_handler(self,handler):
        self._next = handler
    
    @abstractmethod
    def handle(self,request):
        pass

class Handler50(BaseHandler):
    def handle(self,request):
        if request >= 50:
            amount = request // 50
            remainder = request % 50
            print(f'dispensing {amount} 50$')
            if remainder != 0:
                # print('remainder: ',remainder)
                self._next.handle(remainder)    
        else:
            self._next.handle(request)
class Handler20(BaseHandler):
    def handle(self,request):
        if request >= 20:
            amount = request // 20
            remainder = request % 20
            print(f'dispensing {amount} 20$')
            if remainder != 0:
                # print('remainder: ',remainder)
                self._next.handle(remainder)    
        else:
            self._next.handle(request)

class Handler10(BaseHandler):
    def handle(self,request):
        if request >= 10:
            amount = request // 10
            remainder = request % 10
            print(f'dispensing {amount} 10$')
            if remainder != 0:
                self._next.handle(remainder)    
        else:
            self._next.handle(request)

        
class Chain():
    def __init__(self):
        self.handler_1 = Handler50()
        self.handler_2 = Handler20()
        self.handler_3 = Handler10()
        self.handler_1.set_next_handler(self.handler_2)
        self.handler_2.set_next_handler(self.handler_3)
    
    def __call__(self,request):
        self.handler_1.handle(request)

if __name__ == '__main__':
    chain = Chain()
    request = 180
    print('request 180$')
    chain(request)


