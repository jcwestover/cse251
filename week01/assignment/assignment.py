'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

from unittest import TestCase
from cse251functions import *


def perform_math(initial_value: int, value: int, operation: str) -> float:
    '''
    Description
        performs mathematical operations based on user input

    Parameters
        initial value (int): first int in mathematical equation
        value (int): second int in mathematical equation
        operation (str): operator you would like to use in the equation

    Return
        answer (float): result of the mathematical operation
    '''
    # python's "switch" statement. Used to determine the calculation needed based on user input
    match operation:
        case '+':
            answer = initial_value + value
        
        case '-':
            answer = initial_value - value

        case '*':
            answer = initial_value * value

        case '/':
            answer = initial_value / value

        case '//':
            answer = initial_value // value

        case '**':
            answer = initial_value ** value
    
    return answer



def find_word_index(word_to_find: str, words: list) -> int:
    '''
    Description
        returns the index value of a specific value in list based on user input

    Parameters
        word_to_find (str): value you would like to find the index for in the list
        words (list): list that contains the value you would like to find the index to

    Return
        value (int): index value of word_to_find in the words list 
    '''
    #using index method in order to find the value (int) of word_to_find in the words list
    value = words.index(word_to_find)
    
    return value


def get_value_from_dict_using_key(key: str, word_dict: dict) -> str:
    '''
    Description
        returns the value mapped to the given key from the given dictionary

    Parameters
        key (str): key to find its mapped value in the dictionary
        word_dict (dict): dictionary which contains the key - value pairs you would like to access

    Returns
        value (str): the value of the entered key
    '''
    #using .get method in order to find the value of the entered key in the given dictionary
    value = word_dict.get(key)

    return value


def get_list_of_urls_from_dict(key: str, url_dict: dict) -> list:
    '''
    Description
        Gets the value mapped to 'key' in url_dict

    Parameters
        key (str): key whose value will be returned
        url_dict (dict): dictionary which contains the key-value pairs you would like to access

    Return
        value (list): list mapped to the given key
    '''
    value = url_dict.get(key)

    return value


def find_url(urls: list, name: str) -> str:
    '''
    Description
        Returns the url that contains the name within a list of urls

    Parameters
        urls (list): list of urls
        name (str): name you would like to search for within the list of urls

    Return
        value (str): The url that contains the given name (if found)
        "": if no url is found that containes the given name
    '''
    #loops through all urls
    for url in urls:

        #if name is found in url it reutrns that url. else returns empty str
        if name in url:
            return url
    return ""


def find_str_in_file(filename: str, str_to_find: str) -> bool:
    '''
    Description
        returns true if str_to_find in within the file, else false

    Parameters
        filename (str): filename that will be used to search for str_to_find
        str_to_find (str): string that will be searched for in filename

    Return
        (bool): True if str_to_find is within the file, else False
    '''
    #opens file with same name as passed name
    with open(filename, 'r') as file:

        #iterates through lines in file
        for line in file:

            #if str_to_find is found in the current line it will return True, else False
            if str_to_find in line:
                return True
    return False


class MyParentClass:
    '''
    Description
        creates a class with three parameters

    Parameters
        value (int)
        values (list)
        name (str)
    '''

    #constructor for MyParentClass
    def __init__(self, value: int, values: list, name: str) -> None:
        self.value = value
        self.values = values
        self.name = name

    def get_value_using_index(self, index: int):
        '''
        Description
            returns the value in the values list at an index that is passed in

        Parameteres
            index (int): index that will be used to find the desired value in values list

        Return
            value at passed in input in values list
        '''
        return self.values[index]


class MyChildClass(MyParentClass):
    '''
    Description
        creates a class that extended MyParentClass

    Parameters
        value (int)
        values (list)
        name (str)
        age (int)
    '''

    #constructor for MyChildClass
    def __init__(self, value: int, values: list, name: str, age: int) -> None:
        super().__init__(value, values, name)
        self.age = age


        '''Pass by reference means that changes made to an object (in this case a list) inside a function will also be made to the original data in global scope.'''


def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable: list, str_to_add: str) -> str:
    '''
    Description
        appends str_to_add to list and returns index 0 (zero)

    Parameters
        lists_are_passed_by_reference_and_mutable (list): List that str_to_add will be appended to.
        str_to_add (str): string that will be added to lists_are_passed_by_reference_and_mutable 

    Return
        returns index 0 (zero) if lists_are_passed_by_reference_and_mutable
    '''
    lists_are_passed_by_reference_and_mutable.append(str_to_add)
    return lists_are_passed_by_reference_and_mutable[0]


'''immutable means that a data type cannot be changed.'''


def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable: str, str_to_add: str) -> str:
    '''
    Description
        appends str_to_add to strings_are_pass_by_reference_and_immutable

    Parameters
        strings_are_pass_by_reference_and_immutable (str): string that str_to_add will be appended to
        str_to_add (str): string that will be appended to strings_are_pass_by_reference_and_immutable
    
    Return
        (str) appened string
    '''
    return strings_are_pass_by_reference_and_immutable + str_to_add

# Don't change any of the assert lines. All asserts should pass. You should see "All tests passed!" if all assert pass.
# If an assert doesn't pass, you will see an AssertionError (see https://www.w3schools.com/python/ref_keyword_assert.asp).
# The AssertionError will show you why it didn't pass (meaning, it is not an error with the assertion code, but with your code)

def main():
    ''' Know how to:
        - Call a function
        - Pass in parameters to a function in the correct order
        - Use correct parameter data types
        - Return a value from a function
        - Return correct data type from a function
        - Return from all call paths in a a function
        - Write an IF statement
        - Reading: https://www.geeksforgeeks.org/python-functions/
    '''
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    ''' Know how to:
        - Use a list
        - Use the index function on a list
        - Reading: https://www.geeksforgeeks.org/python-lists/
    '''
    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    ''' Know how to:
        - Use a dictionary
        - Use a key to get the value in a dictionary
        - Understand that a dictionary value can be list
        - Know how to get the list using a key
        - Know how to write a FOR loop
        - Know how to use "in" keyword
        - Reading: https://www.geeksforgeeks.org/python-dictionary/
    '''
    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10
    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films":
                  ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    '''
        - Know how to make a Python Class
        - Know how to write a constructor
        - Know how to make attributes in a constructor
        - Understand how to use "self" in Python
        - Know how to instantiate an object of a class (shown below)
        - Know how to obtain the value using the object's attribute (shown below)
        - Know what a method is and how to write one
        - Know how to return a value from a method
        - Know to obtain a value at a specific index in a list
        - Know how to extend a class
        - Understand that an extended/child class inherits everything from parent class
        - Readings: https://www.geeksforgeeks.org/python-classes-and-objects/, https://www.geeksforgeeks.org/extend-class-method-in-python/, https://realpython.com/python-super/
    '''
    
    obj = MyParentClass(1, [5, 6, 7], '3')
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7


    childObj = MyChildClass(1, [5, 6, 7], '3', 10)
    assert childObj.value == 1
    assert childObj.values == [5, 6, 7]
    assert childObj.name == "3"
    assert childObj.age == 10
    assert childObj.get_value_using_index(0) == 5
    assert childObj.get_value_using_index(1) == 6
    assert childObj.get_value_using_index(2) == 7
    assert isinstance(childObj, MyParentClass) == True

    '''
        - Know how to open a file
        - Know how to read lines from a file
        - Understand how to compare strings
        - Readings: https://www.geeksforgeeks.org/open-a-file-in-python/, https://www.geeksforgeeks.org/with-statement-in-python/
    '''
    assert find_str_in_file("data.txt", "g") == True
    assert find_str_in_file("data.txt", "1") == False

    '''
        - Know the difference between pass-by-reference and pass-by-value.
        - Reading: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference (read the first answer)
        - Technically python is pass-by-object-reference, if you are intested in the difference, read https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
    '''
    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"
    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(
        s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")


if __name__ == '__main__':
    main()
    create_signature_file()
 