'''
Requirements
1. Write a multithreaded program that calls a local web server. The web server is 
   provided to you. It will return data about the Star Wars movies.
2. You will make 94 calls to the web server, using 94 threads to get the data.
3. Using a new thread each time, obtain a list of the characters, planets, 
   starships, vehicles, and species of the sixth Star Wars movie.
3. Use the provided print_film_details function to print out the data 
   (you can modify it if you need).
   
Questions:
1. Is this assignment an IO Bound or CPU Bound problem (see https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)?
    > IO bound since we are waiting on speed of the server rather than speed of the CPU
2. Review dictionaries (see https://isaaccomputerscience.org/concepts/dsa_datastruct_dictionary). How could a dictionary be used on this assignment to improve performance?
    > Dicitionaries can be used to improve performance of the program by creating more efficient storage functions. (storing results)
'''


from datetime import datetime, timedelta
import time
import requests
import json
import threading
from cse251functions import *

#creating a thread lock
lock = threading.Lock()

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
CALL_COUNT = 0


# creating a thread class called api_thread
class api_thread(threading.Thread):

    # initializing with URL, result dictionary, and key
    def __init__(self, url, result_dict, key):
        threading.Thread.__init__(self)
        self.url = url
        self.result_dict = result_dict
        self.key = key
    
    # defining a behavior named run in the api_thread class
    def run(self):

        # getting the CALL_COUNT variable from global scope
        global CALL_COUNT

        # Get request to the url
        response = requests.get(self.url)

        # set data to jjson of the get request (above)
        data = response.json()

        # use lock to preserve data
        with lock:

            # creating a key if it doesnt exist
            if self.key not in self.result_dict:
                self.result_dict[self.key] = []

            self.result_dict[self.key].append(data)
            CALL_COUNT += 1



def print_film_details(film, chars, planets, starships, vehicles, species):
    '''
    Print out the film details in a formatted way
    '''
    
    def display_names(title, name_list):
        print('')
        print(f'{title}: {len(name_list)}')
        names = sorted([item["name"] for item in name_list])
        print(str(names)[1:-1].replace("'", ""))

    print('-' * 40)
    print(f'Title   : {film["title"]}')
    print(f'Director: {film["director"]}')
    print(f'Producer: {film["producer"]}')
    print(f'Released: {film["release_date"]}')

    display_names('Characters', chars)
    display_names('Planets', planets)
    display_names('Starships', starships)
    display_names('Vehicles', vehicles)
    display_names('Species', species)


def main():
    #Start a timer
    begin_time = time.perf_counter()
    
    print('Starting to retrieve data from the server')

    # dictionaries to hold results from the initial api calls
    top_api_result = {}
    film_6_result = {}

    # threads for initial api calls
    top_api_thread = api_thread(TOP_API_URL, top_api_result, 'top_api')
    film_6_thread = api_thread(f'{TOP_API_URL}/films/6', film_6_result, 'film_6')

    # sttart initial call threads
    top_api_thread.start()
    film_6_thread.start()

    top_api_thread.join()
    film_6_thread.join()

    # getting results from the first 2 api calls
    api_data = top_api_result['top_api'][0]
    film_6_data = film_6_result['film_6'][0]

    # list of categroies
    categories = ['characters', 'planets', 'starships', 'vehicles', 'species']

    # dictionary for results
    results = {cat: [] for cat in categories}

    # thread list
    threads = []

    # iterate through category using list
    for cat in categories:

        # go thorugh each url
        for url in film_6_data[cat]:

            # creat a thread for each url
            thread = api_thread(url, results, cat)
            threads.append(thread)
            thread.start()

    # waiting for all threads to complete
    for thread in threads:
        thread.join()



    print_film_details(film_6_data, results['characters'], results['planets'], results['starships'], results['vehicles'], results['species'])

    print(f'There were {CALL_COUNT} calls to the server')
    total_time = time.perf_counter() - begin_time
    total_time_str = "{:.2f}".format(total_time)
    print(f'Total time = {total_time_str} sec')
    
    # If you do have a slow computer, then put a comment in your code about why you are changing the total_time limit. Note: 90+ seconds means that you are not doing multithreading
    assert total_time < 15, "Unless you have a super slow computer, it should not take more than 15 seconds to get all the data."
    
    assert CALL_COUNT == 94, "It should take exactly 94 threads to get all the data"
    

if __name__ == "__main__":
    main()
    create_signature_file()