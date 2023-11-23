class Node():
    def __init__(self):
        self.__children = []
        self.__value = None
        self.__parent = None
    def add(self,node):
        self.__children.append(node)
        node.set_parent(self)    

    def set_parent(self,parent):
        self.__parent = parent

    def remove_child(self,child):
        self.__children.remove(child)
        del child

    def __del__(self):
        for i in self.__children:
            del i

class Tree():
    def __init__(self,list_nodes):
        pass 
    def display_tree(self):
        pass
    def __height():
        pass

    def sort():
        pass
