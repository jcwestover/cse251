import threading
import time
import random
import queue


def test_with_barrier(barrier: threading.Barrier, q: queue.Queue):
    print(f'{threading.current_thread().name}: BEFORE SLEEP time={time.time()}\n', end="")
    time.sleep(random.uniform(0.1, 1.0))
    q.put(time.time())
    print(f'{threading.current_thread().name}: AFTER SLEEP time={time.time()}\n', end="")
    
    barrier.wait()
    print(f'{threading.current_thread().name}: AFTER WAIT time={time.time()}\n', end="")
    q.put(time.time())

if __name__ == '__main__':
    
    NUMBER_OF_THREADS = 4
    
    q = queue.Queue()
    
    barrier = threading.Barrier(NUMBER_OF_THREADS)
    
    threads = []
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=test_with_barrier, args=(barrier, q))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    for _ in range(q.qsize()):
        print(f'{q.get()}')