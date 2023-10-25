import multiprocessing
import os
import time

def square(n):
    n **= 2
    print(f'{multiprocessing.current_process().name}: {n}')
    time.sleep(0.01)
    return n

if __name__ == '__main__':
    inputs = list(range(100))
    
    count = multiprocessing.cpu_count()
    
    print(f'{count=}')
    
    # pool = multiprocessing.Pool(count)
    
    # output = pool.map(square, inputs)
    #pool.close()
    #pool.join()
    
    output = []
    with multiprocessing.Pool(count) as p:
        output = p.map(square, inputs)
    
    print(f'{output=}')
    
    