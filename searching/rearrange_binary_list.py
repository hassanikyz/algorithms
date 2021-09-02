def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """

    """
    Algorithm:
    Start with two pointers from both ends and swap values which are on the wrong side until the two pointers cross each other -- signaling we are done.
    """
    
    left = 0
    right = len(lst) - 1
    while left < right:

        while left < len(lst) and lst[left] == 0:
            left += 1
        
        while left < len(lst) and lst[right] == 1:
            right -= 1

        if left < right and lst[left] == 1 and lst[right] == 0:
            lst[left],lst[right] = lst[right], lst[left]
        
        left += 1
        right -= 1

    return lst


print("Rearranged: ", sort_binary_list([1,0,1,0, 1,1,0,0]))
