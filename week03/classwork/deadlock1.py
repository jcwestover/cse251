import threading
import time

BALANCE = 0

def deposit(money: int, lock: threading.Lock):
    print(f'{threading.current_thread().name}: About to acquire lock\n', end="")
    lock.acquire()
    print(f'{threading.current_thread().name}: Yo, I got the lock\n', end="")
    
    global BALANCE
    print(f'{threading.current_thread().name}: {money=}\n', end="")
    BALANCE = BALANCE + money
    time.sleep(0.1)
    print(f'{threading.current_thread().name}: {BALANCE=}\n', end="")
    
    print(f'{threading.current_thread().name}: About to release lock\n', end="")
    #lock.release()
    print(f'{threading.current_thread().name}: Released the lock\n', end="")

def main():
    
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    
    money = 100
    t1 = threading.Thread(target=deposit, args=(money, lock1, lock2))
    money = -50
    t2 = threading.Thread(target=deposit,args=(money, lock2, lock2))
    
    t2.start()
    t1.start()
    
    t1.join()
    t2.join()

    print(f'All Done: {BALANCE=}')

if __name__ == '__main__':
    main()