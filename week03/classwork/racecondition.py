import threading
import time
import random
import queue

VALUE = 0

def adder(amount: int, repeats: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeats):
        print('adder: about to acquire lock')
        with lock:
            tmp = VALUE
            
            time.sleep(random.uniform(0.0001, 0.001))
            tmp += amount
            
            VALUE = tmp
        print('adder: released lock')
    

def subtractor(amount: int, repeats: int, lock: threading.Lock):
    global VALUE
    for _ in range(repeats):
        print('subtractor: about to acquire lock')
        with lock:
            tmp = VALUE
        
            time.sleep(random.uniform(0.0001, 0.001))
            
            tmp -= amount
            VALUE = tmp
        print('subtractor: released lock')

def main():
    
    threads = []
    
    lock = threading.Lock()
    
    for _ in range(1):
        t1 = threading.Thread(target=adder, args=(1, 1_000, lock))
        t2 = threading.Thread(target=subtractor, args=(1, 1_000, lock))
        threads.append(t1)
        threads.append(t2)
    
    print('waiting for threads to complete...')
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    print(f'{VALUE=}')
    
if __name__ == "__main__":
    main()