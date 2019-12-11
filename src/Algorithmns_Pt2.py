'''
Created on Oct 1, 2019

@author: Aparna Ganesh
'''
import re


def sum_digits(number: int) -> int:
    """ 1. Sums each digit of a number together using recursion
    @param number: an integer whose digits will be summed
    @return: the sum of all digits in the number
    """
    if abs(number) == 0:
        return 0
    return (abs(number) % 10) + sum_digits(abs(number) // 10)



def is_diff_two(values: list, diff: int) -> bool:
    """Checks if there are two elements within a list that have a specific 
    difference between them using recursion
    @param values: The list of integer values to be searched
    @param diff: The difference value between two elements to find
    @return: True if there are two elements in values with a difference of diff 
    otherwise False
    """
    if len(values) == 0 or len(values) == 1:
        return False
    elif iterate (values, 0, len(values) - 1, diff):
        return True
    else:
        return False
    

def iterate (values: list, first: int, last: int, diff: int) -> bool:
    """
    helper function for is_diff_two()
    """
    if first == len(values) - 1:
        return False
    if last == first and first < len(values):
        first = first + 1
        last = len(values) - 1
    if (abs(values[first] - values[last]) == diff):
        return True
    else:
        return iterate(values, first, last - 1, diff)
       
     

def across_bridge(people: list) -> int:
    """ 2. Finds the minimum time for 4 people to cross a bridge.
    It is dark, and it is necessary to use a torch when crossing the bridge,
    but they have only one torch between them. The bridge is narrow, and only two
    people can be on it at any one time. The four people take the given amounts of 
    time to cross the bridge; when two cross together they proceed at the speed 
    of the slowest. The torch must be ferried back and forth across the bridge,
    so that it is always carried when the bridge is crossed.
    @param a list of 4 positive integers representing the times of the 4 people
    @return the minimum amount of time possible for the 4 people to get across the 
    bridge
    """
    people = sort_list(people)
    totalDiff = people[0] - 2*people[1] + people[3]
    sumTimes = 0
    
    if totalDiff <= 0:
        sumTimes = 2*people[0] + people[1] + people[2] + people[3]
    else:
        sumTimes = people[0] + 3*people[1] + people[3]
    
    return sumTimes


def sort_list(peopleList: list) -> list:
    """ Rearranges the list in ascending order of times
    @param a list of 4 positive integers
    @return a list of 4 positive integers in ascending order
    """
   
    for i in range (len(peopleList)):
        for j in range (i + 1, len(peopleList)):
            if (peopleList[i] > peopleList[j]):
                temp = peopleList[i]
                peopleList[i] = peopleList[j]
                peopleList[j] = temp
    return peopleList


def string_allowed(string):
    """
    Write a Python program to check that a string 
    contains only a-z, A-Z, and 0-9 characters
    """
    ch = re.compile(r'[^a-zA-Z0-9.]')
    string = ch.search(string)
    return not bool(string)

print('ABCabd123 is', string_allowed("ABCabd123"))
print('#*%*# =', string_allowed("#*%*#"))


def searchStrings(string: str, alist: list) -> bool:
    """
    Write a Python program to search some literals
    strings in a string
    """

    for i in alist:
        if re.search(i, string):
            return True
        else:
            return False
        
print('Search whether fox, dog, and horse is in the string "The quick brown fox jumps over the lazy dog."', searchStrings( 'The quick brown fox jumps over the lazy dog.', ['fox', 'dog', 'horse'] ))
