import threading
import time

SUM = []

def add_two_number(thread_id: int, num1: int, num2: int):
    global SUM
    print(f'adding {num1} to {num2}\n', end="")
    SUM.append(num1 + num2)
    time.sleep(1)
    print(f'{SUM=}\n', end="")

#sum = add_two_number(10, 20)

threads = []
t1 = threading.Thread(target=add_two_number, args=(0, 1, 2))
threads.append(t1)
t2 = threading.Thread(target=add_two_number, args=(1, 2, 2))
threads.append(t2)
t3 = threading.Thread(target=add_two_number, args=(2, 2, 3))
threads.append(t3)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'All Done: {SUM=}')


