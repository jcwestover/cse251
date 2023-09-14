from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any


def myFunction(a: int, b: int) -> int:
    print(f'a={id(a)}')
    print(f'b={id(b)}')
    a = 5
    b = 10
    print(f'IN FUNCTION, AFTER a={id(a)}')
    print(f'IN FUNCTION, AFTER b={id(b)}')
    return a + b

x = 1 # int
y = 2 # int
print(f'x={id(x)}')
print(f'y={id(y)}')
myFunction(x, y)
print(f'AFTER x={id(x)}')
print(f'AFTER y={id(y)}')
print(f'AFTER x={x}')
print(f'AFTER y={y}')

def my_function_list(l : list):
    l.append("hello")

# mutable vs immutable
myList = []
my_function_list(myList)
print(myList)

def my_function_string(s : str):
    s = s.capitalize()
    print("INSIDE FUNCTION s=", s)
    return "B" in s
    
myString = "abcdef"
is_a_in_myString = my_function_string(myString)
print(myString)
print(f'a is in the string = {is_a_in_myString}')

def myFunction1(a: int, b: int):
    return a, b

x, y = myFunction1(54, 4309)
print(f'{x=}, {y=}')

t = ('a', 'b', 'c')

d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])
print(d)

class MyClass:
    def __init__(self, count: int, name: str, children_names: list) -> None:
        self.count = count
        self.name = name
        self.children_names = children_names
    
    def print_values(self):
        print(f'{self.count=}, {self.name=}, {self.children_names=}')

my_object = MyClass(1, "Brandon", ["Noah", "Cole", "Matthew", "Anna", "Isaac", "Grant"])
my_object.print_values()

class MyChildClass(MyClass):
    def __init__(self, count: int, name: str, children_names: list, age: int) -> None:
        super().__init__(count, name, children_names)
        self.age = age

my_child_object = MyChildClass(1, "Brandon", ["Noah", "Cole", "Matthew", "Anna", "Isaac", "Grant"], 48)

class MyThread(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
