import multiprocessing as mp
import queue
import ctypes


def sender(count, q, v, connection):
    print(f'sender: {count}')

    #for i in range(count):
    #    q.put(i)
    #    v.value += 1
    #q.put(None)
    
    for i in range(count):
        connection.send(i)
    connection.send(None)


def receiver(q, v, connection):

    #while True:
    #    item = q.get()
    #    print(f'{item=}')
    #    if item == None:
    #        break
    while True:
        item = connection.recv()
        print(f'{item}')
        if item == None:
            break
    
    #print(f'{v.value=}')


def main():
    q = mp.Queue()
    value = mp.Value(ctypes.c_int, 0)
    
    p_parent, p_child = mp.Pipe()

    p1 = mp.Process(target=sender, args=(10, q, value, p_parent))
    p1.start()
    p2 = mp.Process(target=receiver, args=(q, value, p_child))
    p2.start()


print(f'{__name__}: outside of a function')

if __name__ == "__main__":
    main()
