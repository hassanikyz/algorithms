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


lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 84444]
key = 244

# Function call
result = binary_search(lst, 0, len(lst) - 1, key)
if (result == -1): 
    print(f"{key} is not found")
else:
    print(f"{key} is found at {result}")
