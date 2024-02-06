import queue
import threading
import time

def read(q: queue.Queue):
    while True:
        print(f'Getting item from queue')
        item = q.get()
        print(f'Obtained {item}')
        if item is None:
            break

def write(q: queue.Queue):
    time.sleep(3)
    print('Adding "RED" to queue')
    q.put("RED")
    time.sleep(3)
    q.put(None)

q = queue.Queue()

t1 = threading.Thread(target=read, args=(q,))
t2 = threading.Thread(target=write, args=(q,))

t1.start()
t2.start()


print('Started threads...')

t1.join()
t2.join()

print('All Done')