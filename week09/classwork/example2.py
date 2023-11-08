import string
import random
import time
import threading

FOUND_END = False

class FlightPath:
    
    def __init__(self, houses, lock):
        self.houses = houses
        self.my_house = 'Q'
        self.lock = lock
    
    def atEnd(self, house):
        return house == self.my_house
    
    def getStartHouse(self):
        return self.houses.pop(0)
    
    def move(self):
        moveTo = []
        if len(self.houses) > 1:
            with self.lock:
                moveTo.append(self.houses.pop(random.randrange(len(self.houses))))
                moveTo.append(self.houses.pop(random.randrange(len(self.houses))))
            time.sleep(0.1)
        return moveTo
    
def deliver_presents_recursively(flightPath: FlightPath, house, path):
    global FOUND_END
    
    if FOUND_END:
        return True
    if flightPath.atEnd(house):
        print('Santa found my house')
        FOUND_END = True
        path.append(house)
        return   

    path.append(house)
    
    nextHouses = flightPath.move()
    
    threads = []
    for nextHouse in nextHouses:
        t = threading.Thread(target=deliver_presents_recursively, args=(flightPath, nextHouse, path))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    
    

if __name__ == '__main__':
    houses = list(string.ascii_lowercase + string.ascii_uppercase)
    print(f'{houses}')
    
    path = []
    
    lock = threading.Lock()
    
    flightPath = FlightPath(houses, lock)
    
    startHouse = flightPath.getStartHouse()
    
    deliver_presents_recursively(flightPath, startHouse, path)
    
    print(f'{path=}')
    