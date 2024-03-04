import multiprocessing as mp
from multiprocessing import Value
import queue
import ctypes

def sender(count, q: mp.Queue):
    for i in range(count):
        q.put(i)
    
    q.put(None)

def receiver(q: mp.Queue, stats ):
    while True:
        item = q.get()
        if item == None:
            break
        print(f'{item=}')
        stats.value += 1


def main():
    q = mp.Manager().Queue()
    #q = queue.Queue()
    stats = mp.Manager().Value(ctypes.c_int, 0)
    
    r = mp.Process(target=receiver, args=(q, stats))
    s = mp.Process(target=sender, args=(10, q, ))
    
    r.start()
    s.start()
    
    r.join()
    s.join()
    
    print(f'{stats.value=}')
    

if __name__ == "__main__":
    main()