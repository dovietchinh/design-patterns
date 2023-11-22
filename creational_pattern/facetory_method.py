
"""
Giao việc khởi tạo đối tượng cho đói tượng con
Mục đích:
    Tạo ra một cách khởi tạo object mới thông qua một interface chung
    Che giấu quá trình xử lý logic của phương thức khởi tạo
    Giảm sự phụ thuộc, dễ dàng mở rộng
    Giảm khả năng gây lỗi compile
"""

"""
    # Let's consider following problems.
    # You have a Class represent for Object, and and Action
"""
import json
from uuid import uuid4
from abc import abstractmethod
import xml.etree.ElementTree as ET

class Object1:
    def __init__(self,ob1_first_property,ob1_second_property):
        self.ob1_first_property = ob1_first_property
        self.ob1_second_property = ob1_second_property
    def serialize(self,serializer):
        serializer.start_object('Object1',str(uuid4()))
        serializer.add_property('ob1_first_property',self.ob1_first_property)
        serializer.add_property('ob1_second_property',self.ob1_second_property)

class Object2:
    def __init__(self,ob1_first_property,ob1_second_property):
        self.ob1_first_property = ob1_first_property
        self.ob1_second_property = ob1_second_property

    def serialize(self,serializer):
        serializer.start_object('Object2',str(uuid4()))
        serializer.add_property('ob1_first_property',self.ob1_first_property)
        serializer.add_property('ob1_second_property',self.ob1_second_property)

class SerializeFactory():
        
    def __init__(self):
        self._creator = {}

    def register_creator(self,type):
        def wrapper(func):
            self._creator[type] = func
            return func
        return wrapper
    
    def get_serializer(self,format):
        serializer = self._creator.get(format)
        if not serializer:
            raise ValueError("format error")
        return serializer()
    
    def serialize(self,object,format):
        serializer = factory.get_serializer(format)
        object.serialize(serializer)
        return serializer.to_str()
    
factory = SerializeFactory()

class Serializer():    
    @abstractmethod
    def start_object(self,name,object_id):
        raise NotImplementedError
    
    @abstractmethod
    def add_property(self,name,value):
        raise NotImplementedError
    
    @abstractmethod
    def to_string(self):
        raise NotImplementedError
    
    

@factory.register_creator('json')
class SerializeJSON(Serializer):
    def __init__(self):
        self._current_object = {}

    def start_object(self, name,object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)

@factory.register_creator('xml')
class SerializeXML(Serializer):
    def __init__(self):
        self._element = None
    def start_object(self, object_name, object_id):
        self._element = ET.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = ET.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return ET.tostring(self._element, encoding='unicode')
    


if __name__ == '__main__':
    # factory should be signleton 
    factory = SerializeFactory()
    ob1 = Object1('asdasd','sdfsd')
    result_json = factory.serialize(ob1,'json')
    result_xml = factory.serialize(ob1,'xml')
    print('result_json: ',result_json)
    print('result_xml: ',result_xml)


