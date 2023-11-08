import string
import random
import time

class FlightPath:
    
    def __init__(self, houses):
        self.houses = houses
        self.my_house = 'Q'
    
    def atEnd(self, house):
        return house == self.my_house
    
    def getStartHouse(self):
        return self.houses[0]
    
    def move(self):
        if len(self.houses) > 0:
            moveTo = moveTo = self.houses.pop(random.randrange(len(self.houses)))
            time.sleep(0.1)
            return moveTo
        return None
    
def deliver_presents_recursively(flightPath: FlightPath, house, path):
    
    path.append(house)
    
    if flightPath.atEnd(house):
        return True   
    
    nextHouse = flightPath.move()
    
    if deliver_presents_recursively(flightPath, nextHouse, path):
        print("Santa found my house")
    else:
        print(f"{house} is not my house")
        return False
    
    

if __name__ == '__main__':
    houses = list(string.ascii_lowercase + string.ascii_uppercase)
    print(f'{houses}')
    
    path = []
    
    flightPath = FlightPath(houses)
    
    startHouse = flightPath.getStartHouse()
    
    deliver_presents_recursively(flightPath, startHouse, path)
    
    print(f'{path=}')
    
    