import multiprocessing as mp 
import asyncio

results = []

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

def quotient_all_values(x):
    quotient = 12.8
    for i in range(1, x + 1):
        quotient /= i
    return quotient

def sum_callback(result):
    print(f'{result=}')
    global results
    results.append(result)

if __name__ == "__main__":
    
    pool = mp.Pool(4)
    #results = [pool.apply_async(sum_all_values, args=(x,)) for x in range(10000, 10000 + 10)]
        
    for x in range(10000, 10000 + 10):
        pool.apply_async(sum_all_values, args=(x,), callback=sum_callback)
        
    
    #output = []
    #for r in results:
    #    output.append(r.get())
        
    #output = [p.get() for p in results]
    
    pool.close()
    pool.join()
    print(f'{results=}')