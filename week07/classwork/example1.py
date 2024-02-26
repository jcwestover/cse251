import multiprocessing
import time

SUM = 0

class MyProcess(multiprocessing.Process):
    def __init__(self, loopCount):
        multiprocessing.Process.__init__(self)
        self.loopCount = loopCount
    
    def run(self):
        count(self.loopCount)

def count(loopCount):
    sum = 0
    for i in range(loopCount):
        sum += i
    print(f'{sum=}')
    
    global SUM
    SUM = sum
    

def main():
    #p1 = multiprocessing.Process(target=count, args=(10,))
    #p1.start()
    #p1.join()
    
    p2 = MyProcess(10)
    p2.start()
    p2.join()
    
    print(f'{SUM=}')

print(f'{__name__=}')

if __name__ == '__main__':
    main()