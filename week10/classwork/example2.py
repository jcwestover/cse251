import multiprocessing as mp 

def sum_all_values(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total
    
if __name__ == "__main__":
    pool = mp.Pool(4)
    results = [pool.apply_async(sum_all_values, args=(x,)) for x in range(10000, 10000 + 10)]
    pool.close()
    # do something else
    print("I did not block")

    # collect all of the results into a list
    output = [p.get() for p in results]
    print(output)