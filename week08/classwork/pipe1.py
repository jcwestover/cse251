import multiprocessing as mp
from multiprocessing.connection import PipeConnection

def sender(count, conn: PipeConnection):
    for i in range(count):
        conn.send(i)
    
    conn.send(None)

def receiver(conn: PipeConnection):
    while True:
        item = conn.recv()
        if item == None:
            break
        print(f'{item=}')

def main():
    conn_recv, conn_send = mp.Pipe()
    
    r = mp.Process(target=receiver, args=(conn_recv,))
    s = mp.Process(target=sender, args=(10, conn_send))
    
    r.start()
    s.start()
    
    r.join()
    s.join()
    

if __name__ == "__main__":
    main()