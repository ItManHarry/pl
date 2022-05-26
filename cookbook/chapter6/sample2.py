'''
Reading and Writing JSON Data
Problem
    You want to read or write data encoded as JSON (JavaScript Object Notation).
Solution
    The json module provides an easy way to encode and decode data in JSON. The two
main functions are json.dumps() and json.loads(), mirroring the interface used in
other serialization libraries, such as pickle
'''
# to string
import json
data = {
    'name': 'Harry',
    'age': 40,
    'email': 'guoqian.cheng@hyundai-di.com'
}
js = json.dumps(data)
print(type(js), js)
# string to python
ds = json.loads(js)
print(type(ds), ds)
# to file
with open('data.json', 'w') as f:
    json.dump(data, f)
# file back to python
with open('data.json') as f:
    ds = json.load(f)
print(ds)
data = {
    'Name': 'Harry',
    'Man': True,
    '40': 40
}
js = json.dumps(data)
print(js)
print('-' * 80)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(10, 20)
# 序列化Python对象
def serialize_instance(obj):
    b = {'__classname__': type(obj).__name__}
    b.update(vars(obj))
    return b
jp = json.dumps(serialize_instance(p))
print(jp)
# 反序列化Python对象
def unserialize_instance(d):
    classes = {
        'Point': Point
    }
    classname = d.pop('__classname__', None)
    if classname:
        cls = classes[classname]
        obj = cls.__new__(cls)  # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d
jp = json.dumps(p, default=serialize_instance)
p = json.loads(jp, object_hook=unserialize_instance)
print(p)
print(p.x)
print(p.y)