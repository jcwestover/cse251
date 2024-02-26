import multiprocessing as mp
import time

def square(n):
    n **= 2
    time.sleep(0.1)
    return n

def main():
    
    inputs = list(range(101))
    
    outputs = []
    with mp.Pool(mp.cpu_count()) as p:
        outputs = p.map(square, inputs)
    
    print(f'{outputs=}')

if __name__ == '__main__':
    main()