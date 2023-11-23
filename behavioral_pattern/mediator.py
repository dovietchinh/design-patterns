"""
component send event as a notify to mediator that:
"Hey, I'm doing something, you should know that"
"""
class BaseComponent():
    def __init__(self):
        pass

    @property
    def mediator(self):
        return self._mediator
    
    @mediator.setter
    def mediator(self,value):
        self._mediator = value
    

class Component1(BaseComponent):
    def do_a(self):
        print('component 1 do a')
        self._mediator.notify(self,'A')
    def do_b(self):
        print('component 1 do b')
        self._mediator.notify(self,'b')

class Component2(BaseComponent):
    def do_c(self):
        print('component 2 do c')
        self._mediator.notify(self,'C')
    def do_d(self):
        print('component 2 do d')
        self._mediator.notify(self,'D')

    
class Mediator():
    def __init__(self, component_1,component_2):
        self._component_1 = component_1
        self._component_2 = component_2
        self._component_1.mediator = self
        self._component_2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event=='A':
            print('mediator is doing something to handle event A')
        elif event=='B':
            print('mediator is doing something to handle event B')
        elif event=='C':
            print('mediator is doing something to handle event C')
        else:
            print("I don't know that type of event, just ignore it !!!")


if __name__ == '__main__':
    c1 = Component1()
    c2 = Component2()
    mediator = Mediator(c1,c2)

    c1.do_a()
    c2.do_c()