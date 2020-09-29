"""
Write a function that takes in a two-dimensional list (a list that contains
lists) and returns a new list which contains only the lists from the original
which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or
strings. Also, for this challenge, we are assuming that empty arrays are not
homogenous. Also, the resultant lists should be in the same order as the
original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should
return `[[1, 5, 4], ['b']]`.
"""
#def filter_homogenous(arrays):
    # Your code here

def filter_homogenous(arrays):
   return [a for a in arrays if len(set(list(map(type, a)))) == 1]
print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]))

def digitsManipulations(n):
    #cast the numbers to a string
    # assign product variable starting at 1 (because the integer * itself would = 0)
    # assign sum var
    numbers = str(n)
    numbers_product = 1 
    numbers_sum = 0 
    for number in numbers:
        integer = int(number)
        numbers_product *= integer
        numbers_sum += integer
    return numbers_product - numbers_sum

print(digitsManipulations(4357))