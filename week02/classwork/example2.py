from collections.abc import Callable, Iterable, Mapping
import threading
import time
import random
from typing import Any

SIZE = 500

class MyThread(threading.Thread):
    def __init__(self, a: int, b: int, results: list, id: int):
        super().__init__()
        self.a = a
        self.b = b
        self.results = results
        self.id = id
        
    def run(self):
        time.sleep(1.0) #doing something fancy
        #self.results.append(self.a + self.b)
        self.results[self.id] = self.a + self.b
        print(f'{threading.current_thread()}\n', end="")

def main():

    results = [0] * SIZE
    threads = []
    
    for i in range(SIZE):
        t = MyThread(i, 4, results, i)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    print(f'{results=}')
    print("All Done")

if __name__ == '__main__':
    main()