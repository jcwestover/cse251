import threading, time

THREADS = 3
ITEMS = 1000000

def thread_function(data: int, index: int, lock: threading.Lock):
    print(f'{threading.current_thread().name} - inside function: {id(data)}\n', end="")
    for i in range(ITEMS):
        data += 1
    print(f'{threading.current_thread().name} - inside function: {id(data)}\n', end="")

def main():    
    data = 0   # Each thread uses its own index into the list
    print(f'{id(data)}')
    start_time = time.perf_counter()
    
    lock = threading.Lock()

    # Create threads
    threads = []
    for index in range(THREADS):
        t = threading.Thread(target=thread_function, args=(data, index, lock))
        threads.append(t)
        
    #threads = [threading.Thread(target=thread_function, args=(data, index)) for index in range(THREADS)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'at the end: {id(data)}')
    print(f'All work completed: {data:,} in {time.perf_counter() - start_time:.5f} seconds')

if __name__ == '__main__':
    main()     