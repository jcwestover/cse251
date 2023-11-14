import multiprocessing as mp
import time

result_list = []

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def log_result(result):
    # This is called whenever sum_all_values(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    print(f'log_result: {result}')
    result_list.append(result)

def apply_async_with_callback():
    pool = mp.Pool(4)

    # Add job to the pool
    pool.apply_async(sum_all_values, args = (10000, ), callback = log_result)
    
    time.sleep(1)       # Do something - this is the main thread sleeping

    pool.apply_async(sum_all_values, args = (10001, ), callback = log_result)

    time.sleep(1)       # Do something

    pool.apply_async(sum_all_values, args = (10002, ), callback = log_result)

    time.sleep(1)       # Do something

    pool.apply_async(sum_all_values, args = (10003, ), callback = log_result)

    # Do something while the processes are doing their work

    # Need to know when the pool is finished
    pool.close()
    pool.join()

    print('Finished')

    # display the global variable of the results from the pool
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()