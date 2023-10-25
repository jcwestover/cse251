import multiprocessing
import queue
import time
import threading

def sender(q: multiprocessing.Queue, data):
    for i in range(10):
        data.append(i)
        #q.put(i)
    #q.put(None)
    
    time.sleep(0.1)
    print(f'sender: {data}, id={id(data)}\n', end="")

def main():
    
    lock = multiprocessing.Lock()
    q1 = multiprocessing.Queue()
    
    data = [0] * 10
    
    m_data = multiprocessing.Manager().list()
    
    p1 = multiprocessing.Process(target=sender, args=(q1, m_data))
    p2 = multiprocessing.Process(target=sender, args=(q1, m_data))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f'{m_data}, id={id(m_data)}')

if __name__ == '__main__':
    main()