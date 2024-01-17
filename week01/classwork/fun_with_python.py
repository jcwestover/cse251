from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any

class MyClass:
    def __init__(self, height: int) -> None:
        self.height = height
    
    def print_height(self):
        print(f'{self.height=}')
        
class MyExtendedClass(MyClass):
    def __init__(self, age: int, height: int):
        super().__init__(height)
        self.age = age
    
    def print_age(self):
        print(f'{self.age=}')
        
my_extended_class = MyExtendedClass(7, 30)
my_extended_class.print_age()

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("my thread is running!!")

def fun(my_int, my_str, my_obj) -> None:
    print(my_int)
    print(my_str)
    print(my_obj)

# a list is mutable (it can be modified in-place)
my_list = []
#fun("dsfdsa", 10, my_list)

xyz = MyClass(50)
#print(xyz.my_parameter)
#print(id(xyz))

def modify_string(s):
    print(f'inside modify_string: {id(s)}')
    s = "hijklmn"
    print(f'after modified: inside modify_string: {id(s)}')

# string are immutable
my_string = "abcdefg"
#modify_string(my_string)
#print(f'outside function {id(my_string)}')

def modify_int(i):
    print(f'inside modify_int: {id(i)}')
    i += 10
    print(f'after modified: inside modify_int: {id(i)}')

i = 20
#modify_int(i)
#print(f'outside function {id(i)}')

def modify_list(my_list: list):
    print(f'inside modify_list: {id(my_list)}')
    my_list.append(10)
    print(f'after modified: inside modify_list: {id(my_list)}')

#modify_list(my_list)
#my_list.append(6)
#print(f'outside modify_list: {id(my_list)}')

def modify_dict(d: dict) -> None:
    print(f'inside my_dictionary: {id(d)}')
    my_dictionary["d"] = 4
    print(f'after modified: inside my_dictionary: {id(d)}')

# a dictionary is mutable
my_dictionary = {"a" : 1, "b" : 2, "c" : 3}
print(f'outside modify_dict: {id(my_dictionary)}')
modify_dict(my_dictionary)

my_list = [1, 2, 3]
my_list.append(4)
my_tuple = (1, 2, 3)
