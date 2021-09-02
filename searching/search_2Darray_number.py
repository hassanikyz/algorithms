def binary_search(lst, left, right, key):
    """
    Binary search function
    :param lst: lst of sorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """
    
    # terminate the search if left pointer crosses the right
    # However, each time find the middle index and see if that has the key. If element found at mid index is greater thant key then we can ignore
    # the right half including the mid index of the list. Otherise left half including the mid index is ignored.
    # Ignoring half of the sorted list is done by moving the left or right pointer to left or right side of the mid.
    while left <= right:
        mid = left + ( right - left )//2
        if key == lst[mid]:
            return mid
        
        if key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1



    return -1

def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    # for every row do a binary search for the number we are searching for

    if lst is None:
        return 
    
    for row in lst:
        if binary_search(row, 0, len(row) - 1, number) != -1:
            return True
    

    return False

print("Found = ", find_in([[10, 11, 12, 13], [14, 15, 16, 17], [27, 29, 30, 31], [32, 33, 39, 80]], 35))
