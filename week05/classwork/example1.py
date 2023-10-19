import queue
import threading
import time

NUMBER_DISPLAY_THREADS = 3
DONE = False

def display(i, sem: threading.Semaphore, q: queue.Queue):
    global DONE
    while True:
        print(f'{threading.current_thread().name}: value before acquire = {sem._value}\n', end="")
        #sem.acquire()
        print(f'{threading.current_thread().name}: getting item from queue\n', end="")
        item = q.get()
        print(f'{threading.current_thread().name}: CRITICAL_CODE, value after acquire = {sem._value}\n', end="")
        print(f'{threading.current_thread().name}: {item=}\n', end="")
        if item == "DONE":
            q.put("DONE")
            return

def increment(sem: threading.Semaphore, q: queue.Queue, b: threading.Barrier):
    
    q.put(time.time())
    #sem.release()
    print(f'{threading.current_thread().name}: value after release = {sem._value}\n', end="")
    #sem.release()
    time.sleep(1)
    b.wait()
    print(f'{threading.current_thread().name}: the time is {time.time()}\n', end="")
    q.put("DONE")
    

def main():
    
    q = queue.Queue()
    sem = threading.Semaphore(NUMBER_DISPLAY_THREADS)
    b = threading.Barrier(2)
    
    threads = []
    for i in range(NUMBER_DISPLAY_THREADS):
        t = threading.Thread(target=display, args=(i, sem, q))
        t.start()
        threads.append(t)
    
    t1 = threading.Thread(target=increment, args=(sem, q, b))
    t1.start()
    
    t2 = threading.Thread(target=increment, args=(sem, q, b))
    t2.start()
    
    for t in threads:
        t.join()
    t.join()


if __name__ == '__main__':
    main()