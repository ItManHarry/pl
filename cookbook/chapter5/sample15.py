'''
Serializing Python Objects
Problem
    You need to serialize a Python object into a byte stream so that you can do things such
as save it to a file, store it in a database, or transmit it over a network connection.
Solution
    The most common approach for serializing data is to use the pickle module.
'''
import pickle
data = [1, 2, 3, 4, 5]
f = open('data.bin', 'wb')
pickle.dump(data, f)
f.close()
'''
To dump an object to a string, use pickle.dumps():
'''
data = {1, 2, 3, 4, 5}
s = pickle.dumps(data)
print(s)
# Restore from a file
f = open('data.bin', 'rb')
data = pickle.load(f)
print(data)
data = pickle.loads(s)
print(data)
print('-' * 80)
f = open('serial_data.bin', 'wb')
pickle.dump((1, 2, 3, 4, 5), f)
pickle.dump('HelloPython', f)
pickle.dump({'a': 100, 'b': 200}, f)
pickle.dump(10000, f)
f.close()
f = open('serial_data.bin', 'rb')
'''data = pickle.load(f)
print(data)
data = pickle.load(f)
print(data)
data = pickle.load(f)
print(data)'''
while True:
    try:
        data = pickle.load(f)
        if isinstance(data, (str, dict, int)):
            print('OK')
            print('Data type : ', type(data), ', data is : ', data)
    except:
        print('No more data')
        break
print('-' * 80)
class SysUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'I am {} and I amd {} years old.'.format(self.name, self.age)
u = SysUser('Harry', 40)
print(u)
s = pickle.dumps(u)
print(s)
u = pickle.loads(s)
print(u.name)
print(u.age)