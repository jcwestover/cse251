import threading
import time
import random

SUM = -99999

def add_two_number(a: int, b: int, results: list, id: int):
    print(f'{threading.current_thread()}')
    global SUM
    time.sleep(random.uniform(0.5, 1.0))
    SUM = a + b
    results[id] = a + b

def main():
    results = [0] * 2
    my_thread_0 = threading.Thread(target=add_two_number, args=(2, 4, results, 0))
    my_thread_1 = threading.Thread(target=add_two_number, args=(1, 3, results, 1))
    my_thread_0.start()
    my_thread_1.start()
    
    # go and do something else
    
    my_thread_0.join()
    my_thread_1.join()
    print(f'{SUM=}')
    print(f'{results=}')

if __name__ == '__main__':
    main()