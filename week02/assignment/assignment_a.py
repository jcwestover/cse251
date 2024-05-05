'''
Requirements:
1. Write a function that takes a number and computes the product of all numbers between
   one and that number (exclusive). This will be the target of your thread.
2. Create a thread to run this function.
3. Assert that your products are correct for the given number.
4. COMMENT every line that you write yourself.
   
Things to consider:
a. What is the correct syntax for creating a thread with one argument?
   (see https://stackoverflow.com/questions/3221655/python-threading-string-arguments)
b. How do you start a thread? (see this week's reading) 
c. How will you wait until the thread is done? (see this week's reading)
d. Do threads (including the main thread) share global variables? (see https://superfastpython.com/thread-share-variables/)
e. How will you ensure that one thread doesn't change the value of
   your global while another thread is using it too? (We haven't learned about locks yet, so you
   won't be able to run your threads simultaneously)
f. How do you modify the value of a global variable (see https://stackoverflow.com/questions/10588317/python-function-global-variables)
'''
import threading
from cse251functions import *

# global variable to keeping track of the final product
PRODUCT = 1

def my_function(number):
   '''
   Description
      takes inputed number and calculates the product of all numbers between 1 and the given number.

   Parameters
      number: number that will be used in the calculation

   Return
      PRODUCT
   '''
   # Access global var
   global PRODUCT

   PRODUCT = 1

   # Iterates through range from 1 up till the number that was input
   for i in range(1, number):

      # multiplies PRODUCT var by the number i and then reassigns the PRDOUCT var to that product
      PRODUCT *= i 


def main():
    
   thread5 = threading.Thread(target=my_function, args=(5,))
   thread10 = threading.Thread(target=my_function, args=(10,))
   thread15 = threading.Thread(target=my_function, args=(15,))

   thread5.start()
   thread5.join()

   assert PRODUCT == 24, f'The product should equal 24 but instead was {PRODUCT}'

   thread10.start()
   thread10.join()

   assert PRODUCT == 362880, f'The product should equal 362880 but instead was {PRODUCT}'

   thread15.start()
   thread15.join()

   assert PRODUCT == 87178291200, f'The product should equal 87178291200 but instead was {PRODUCT}'

if __name__ == '__main__':
    main()
    print("DONE")
    create_signature_file()