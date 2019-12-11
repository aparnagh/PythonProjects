'''
Created on Oct 14, 2019

@author: Aparna Ganesh
'''

def log_base_2(number: float) -> str:
    """ 1. Gives the approximate log base 2 calculation of the input number
    @param number: float to calculate on
    @precondition: number is > 0
    @return str: A string description of the approximate result
    """ 
    i = 0
    j = True
    while j:
        if (number >= 1.0):
            if (pow(2, i) > number):
                j = False
                string = 'between ' + str(i - 1) + ' and ' + str(i)
                return (string)
        
            elif (pow(2, i) == number):
                j = False
                string = str(i)
                return (string)
            
            else:
                i = i + 1
        else:
            if (pow(2, i) < number):
                j = False
                string = 'between ' + str(i) + ' and ' + str(i + 1)
                return (string)
        
            elif (pow(2, i) == number):
                j = False
                string = str(i)
                return (string)
            
            else:
                i = i - 1
                

def reverse_list(aList: list) -> list:
    """ 2.Gives a list with the elements in reversed order
    @param aList: list input that's going to be reversed
    @return list: the reversed version of the input list
    """
    size  = len(aList)
    
    for i in range(0, size//2):
        size = size - 1
        temp = aList[i]
        aList[i] = aList[size]
        aList[size] = temp
    return aList


def max_difference(values: list) -> float:
    """ Efficiently finds the largest difference between any two elements in a list
    @param values: a list of numbers
    @return number for the largest difference between elements
    """
    largest = values[0]
    smallest = values[0]
        
    for i in range(0, len(values)):      
        if (values[i] < smallest):
            smallest = values[i]
        if (values[i] > largest):
            largest = values[i]
    
    return largest - smallest
    

def sort_bivalued(values: list) -> list:
    """Efficiently sort a list of binary values
    @param values: a list of binary digits (0 or 1)
    @return: a list of binary numbers in ascending sort order
    """
    start = 0
    end = len(values) - 1
    while start < end:
        if values[start] == 0:
            start += 1
        elif values[end] == 1:
            end -= 1
        elif end > start:
            values[start] = 0
            values[end] = 1
            start += 1
            end -= 1
        else:
            break
    return values
