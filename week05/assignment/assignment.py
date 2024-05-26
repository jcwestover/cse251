'''
Requirements
1. Using two threads, put space ships onto a shared queue, with one thread consuming
   the items from the queue and the other producing the items.
2. The size of queue should never exceed 10.
3. Do not call queue size to determine if maximum size has been reached. This means
   that you should not do something like this: 
        if q.size() < 10:
   Use the blocking semaphore function 'acquire'.
4. Produce a Plot of count vs queue size (okay to use q.size since this is not a
   condition statement).
5. COMMENT every line that you write yourself.
   
Questions:
1. Do you need to use locks around accessing the queue object when using multiple threads? 
   Why or why not?
   >Yes because if you do not it may cause race conditions and data corruption.
   >
2. How would you define a semaphore in your own words?
   > It controls access to a resource (in the case of this assignment, the queue). I does this by acquiring access and then releasing access so only the desired number of threads have access to the resource at once.
   >
3. Read https://stackoverflow.com/questions/2407589/what-does-the-term-blocking-mean-in-programming.
   What does it mean that the "join" function is a blocking function? Why do we want to block?
   > The join function is a blocking function because it will cause the thread to wait (or block it) until the thread has finished running. We want to block in order to ensure the thread has finished its tasks before the program moves on.
   >
   >
'''

from datetime import datetime
import time
import threading
import random
import string
# DO NOT import queue

from plots import *
from cse251functions import *

# Global Constants
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

#########################
# NO GLOBAL VARIABLES!
#########################


class SpaceShip():
    """ This is the SpaceShips class that will be created by the starports """

    # Class Variables
    spaceship_makes = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto')

    spaceship_models = [f'{random.choice(string.ascii_uppercase)}{n}' for n in range(20)]

    spaceship_years = [i for i in range(2100, 2150)]

    def __init__(self):
        # Make a random spaceship
        self.model = random.choice(SpaceShip.spaceship_makes)
        self.make = random.choice(SpaceShip.spaceship_models)
        self.year = random.choice(SpaceShip.spaceship_years)

        # Sleep a little
        time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))

        # Display the spaceship that has just be created in the terminal
        self.display()

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class NonBlockingQueue():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)
        if(len(self.items) > MAX_QUEUE_SIZE):
            raise Exception("You have exceeded the size of your space queue!!!\nYou have broken the law and the Solar System Space Force are coming for you...!!!\nYou need to use semaphore.acquire to block when the queue is full, and call semaphore.release after removing a spaceship from the queue.")

    """Will throw an error if called when there are no items (list is empty)"""
    def get(self):
        if(len(self.items) == 0):
            raise Exception("You are trying to pop an item from your queue, but your queue is empty!\nYou must use a semaphore.acquire to block to prevent this from happening. Call semaphore.release after you put a spaceship on the queue, this will unblock the semaphore.acquire.")
        return self.items.pop(0)


class SpaceShipFactory(threading.Thread):
    """ This is a factory.  It will create spaceships and place them on the queue """

    def __init__(self, count, semaphore_full, semaphore_empty, queue, lock):
        super().__init__()
        
        # spaceships to create
        self.count = count

        # semaphore signal full queue
        self.semaphore_full = semaphore_full

        # semaphore signal empty queue
        self.semaphore_empty = semaphore_empty

        #queue
        self.queue = queue

        # lock for accessing queue
        self.lock = lock

    def run(self):
        for _ in range(self.count):
            # pause if the queue is full
            self.semaphore_empty.acquire()

            # produce spaceship
            spaceship = SpaceShip()

            # access queue
            with self.lock:
                
                # queue spaceship
                self.queue.put(spaceship)

            # use semaphore to singal queue is not empty
            self.semaphore_full.release()


class SpaceShipBuyer(threading.Thread):
    """ This is a buyer that receives spaceships from the queue """

    def __init__(self, semaphore_full, semaphore_empty, queue, lock, stats, total_to_produce):
        super().__init__()
        # semaphore for a full queue
        self.semaphore_full = semaphore_full

        # semaphore for empty queue
        self.semaphore_empty = semaphore_empty

        # queue
        self.queue = queue

        # lock for accessing queue
        self.lock = lock

        # keeps track of sizes of queues
        self.stats = stats

        # number of spaceships to produce
        self.total_to_produce = total_to_produce

        # counter for the processed ships
        self.spaceships_processed = 0

    def run(self):
        while self.spaceships_processed < self.total_to_produce:
            # if queue is empty wait
            self.semaphore_full.acquire()
            
            #access queue
            with self.lock:

                # get spaceship from the queue
                spaceship = self.queue.get()

                # increment queue size counter
                self.stats[self.queue.size()] += 1

                # increment process counter
                self.spaceships_processed += 1

            # signal queue is not full
            self.semaphore_empty.release()

            # Sleep a random amount after selling a space ship
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))


def main():
    # Start a timer
    begin_time = time.perf_counter()

    # Number of spaceships the factory will send to the buyer
    spaceships_to_produce = 500

    # Create semaphores
    #semaphore to track items in queue
    semaphore_full = threading.Semaphore(0)

    # semaphore to track queue availability 
    semaphore_empty = threading.Semaphore(MAX_QUEUE_SIZE)

    # Create queue (ONLY use class NonBlockingQueue)
    queue = NonBlockingQueue()

    # Create lock
    lock = threading.Lock()

    # This tracks the size of the queue at the time a spaceship is removed from the queue by the buyer (do it after calling get()). queue_stats[queue.size()] += 1
    buyer_stats = [0] * MAX_QUEUE_SIZE

    # create one spaceship factory
    factory = SpaceShipFactory(spaceships_to_produce, semaphore_full, semaphore_empty, queue, lock)

    # create one spaceship buyer
    buyer = SpaceShipBuyer(semaphore_full, semaphore_empty, queue, lock, buyer_stats, spaceships_to_produce)

    # Start factory and buyer
    factory.start()
    buyer.start()

    #wait for threads to finish
    factory.join()
    buyer.join()

    total_time = "{:.2f}".format(time.perf_counter() - begin_time)
    print(f'Total time = {total_time} sec')
    
    # The number of spaceships that the factory sends to the buyer should be exactly the same
    assert(sum(buyer_stats) == spaceships_to_produce)

    # Plot space ship count vs queue size
    xaxis = [i for i in range(1, MAX_QUEUE_SIZE + 1)]
    plot = Plots()
    plot.bar(xaxis, buyer_stats,
             title=f'{sum(buyer_stats)} Spaceships Produced by {STUDENT_NAME}: Count VS Queue Size', x_label='Queue Size', y_label='Count')


if __name__ == '__main__':
    main()
    create_signature_file()