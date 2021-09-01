"""
Problem statement#
Given a sorted list of n integers that has been rotated an unknown number of times, write some code to find an element in the list. You may assume that the list was originally sorted in an ascending order.

Input#
A sorted list that has been rotated a number of times

Output#
The index of the element

Sample input#
lst = [7, 8, 9, 0, 3, 5, 6]
n = size of the list
key = 3 # Element that is being searched for
Sample output#
result = 4 # Index of the element that was searched for
"""


def binary_search(lst, left, right, key):
    
    while left <= right:
        mid = left + ( right - left )//2
        if key == lst[mid]:
            return mid
        
        if key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """

    # Find the  index of the smallest value and then consider the array to be composed of two sorted arrays.
    # Left of min index is one array (starting with 0th location). Starting with min index 
    # to the end of the array is the second sorted array.

    # perform binary search in both arrays one by one to locate the element

    min_idx = 0
    min_value = lst[min_idx]
    for i in range(1, n):
        if lst[i] < lst[min_idx]:
            min_idex = i
    
    result = binary_search(lst, 0, min_idx - 1, key)
    if result == -1:
        result = binary_search(lst, min_idx, n - 1, key)

    return result
  
lst = [7, 8, 9, 0, 3, 5, 6]
print("Result ", pivoted_binary_search(lst, 7, 3))
