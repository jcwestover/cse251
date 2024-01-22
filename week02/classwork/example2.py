import threading

class MyThread(threading.Thread):
    def __init__(self, num1: int, num2: int):
        super().__init__()
        self.num1 = num1
        self.num2 = num2
        self.sum = 0
    
    def get_sum(self):
        print(f'\t The sum is {self.sum}')
        return self.sum
        
    def run(self):
        print('running\n', end="")
        self.sum = self.num1 + self.num2
    

t1 = MyThread(2, 5)
t1.start()
print(f'BEFORE JOIN: {t1.sum}')
t1.join()
print(f'AFTER JOIN: {t1.sum}')

sum = t1.get_sum()
print(f'AFTER GET SUM: {sum}')