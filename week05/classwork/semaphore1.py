import threading
import time
import random

class QueueTwoFiftyOne():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

def display(sem_full: threading.Semaphore, sem_empty: threading.Semaphore, q:QueueTwoFiftyOne):
    while True:
        print(f'{sem_empty._value=}')
        sem_empty.acquire()
        item = q.get()
        sem_full.release()
        #print(f'{item=}, {q.size()=}')
        time.sleep(random.uniform(0.01, 0.1))
        if item == None:
            break

def increment(sem_full: threading.Semaphore, sem_empty: threading.Semaphore, q:QueueTwoFiftyOne):
    for i in range(100):
        print(f'{sem_full._value=}')
        sem_full.acquire()
        q.put(i)
        sem_empty.release()
        #time.sleep(random.uniform(0.01, 0.1))
    sem_full.acquire()
    q.put(None)
    sem_empty.release()

def main():
    q = QueueTwoFiftyOne()
    sem_full = threading.Semaphore(10)
    sem_empty = threading.Semaphore(0)

    threads = []
    for i in range(1): 
        t1 = threading.Thread(target=display, args=(sem_full, sem_empty, q)) 
        threads.append(t1)
        t2 = threading.Thread(target=increment, args=(sem_full, sem_empty, q))
        threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
    