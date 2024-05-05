'''
Requirements:
1. Create a class that extends the 'threading.Thread' class (see https://stackoverflow.com/questions/15526858/how-to-extend-a-class-in-python). This means that the class IS a thread. 
   Any objects instantiated using this class ARE threads.
2. Instantiate this thread class that computes the product of all numbers 
   between one and that number (exclusive)
3. COMMENT every line that you write yourself.

Things to consider:
a. How do you instantiate a class and pass in arguments (see https://realpython.com/lessons/instantiating-classes/)?
b. How do you start a thread object (see this week's reading)?
c. How will you wait until the thread is done (see this week's reading)?
d. How do you get the value an object's attribute (see https://datagy.io/python-print-objects-attributes/)?
'''

import threading
from cse251functions import *

###############################
# DO NOT USE YOUR OWN GLOBALS #
###############################

# creating MyThread class
class MyThread(threading.Thread):

    # defining constructor of the class with number parameter
    def __init__(self, number):

        # calling constructor
        threading.Thread.__init__(self)

        # storing number parameter as self.number
        self.number = number

        # creating product attribute. initializing as None
        self.product = None

    # defining run method to do calculation
    def run(self):

        # initializing product var as 1
        product = 1

        # iteration through range from 1 to the number passed in the parameter
        for i in range(1, self.number):

            # calulating product by multiplying product by i and then reassigning that value
            product *= i

        # assigning value of product var to self.product 
        self.product = product



def main():
    # instantiating MyThread class with number 5 and assigning it the thread5
    thread5 = MyThread(5)

    # stating thread
    thread5.start()

    # wait for thread to finish
    thread5.join()

    # assert statement for thread5
    assert thread5.product == 24, f'The product should equal 24 but instead was {thread5.product}'

    # instantiating MyThread class with number 10 and assigning it to thread10
    thread10 = MyThread(10)

    # starting thread
    thread10.start()

    # wait for thread to finish
    thread10.join()

    # assert statement for thread10
    assert thread10.product == 362880, f'The product should equal 362880 but instead was {thread10.product}'

    # instantiating MyThread class with number 10 and assigning it to thread10
    thread15 = MyThread(15)

    # start thread
    thread15.start()

    # wait for thread to finish
    thread15.join()

    # assert statement for thread15
    assert thread15.product == 87178291200, f'The product should equal 87178291200 but instead was {thread15.product}'


if __name__ == '__main__':
    main()
    print("DONE")
    create_signature_file()
