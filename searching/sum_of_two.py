def binary_search(lst, left, right, key):
    """
    Binary search function
    :param lst: lst of sorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """

    
    while left <= right:
        mid = left + ( right - left )//2
        if key == lst[mid]:
            return mid
        
        if key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1



    return -1


def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    
    ""
    We first sort the array, iterate through the list and use binary search to find the second element which when added with first gives us the sum sought for
    ""

    lst.sort()

    for i in lst:
        index = binary_search(lst, 0, len(lst) - 1,  n - i)
        if index:
            return [i, n - i]

        """
        O(n) implementation using sets
        """
def find_sum_faster(lst, n):
    
    found_vals = set()
    
    for j in lst:
        if (n-j) in found_vals:
            return [j, n-j]
    
        found_vals.add(j)
            
    return [-1, -1]

### most efficient solution ###
def twoSum(numbers: List[int], target: int) -> List[int]:

    low, high = 0, len(numbers) - 1

    while (high > low):

        if target == numbers[low] + numbers[high]:
            return (low+1, high+1)
        elif target > numbers[low] + numbers[high]:
            low += 1
        else:
            high -= 1

    return [1, -1]

###
def twoSum_vslow(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    low = 0
    high = low + 1

    def binary_search(key, mlist, left, right):

        if len(mlist) == 1:
            if mlist[0] == key:
                return 0

        while (left <= right):

            mid = left + (right - left)//2
            if mlist[mid] == key:
                return mid

            if key < mlist[mid]:
                right = mid - 1
            if key > mlist[mid]:
                left = mid + 1

        return - 1

    high = len(numbers) - 1
    while low < len(numbers):
        first = numbers[low]
        if low < high:
            second = binary_search(target - first, numbers, low+1, high )
            if second != -1:
                return [low+1, second+1]
        low += 1

    return [-1, -1]
            
            
print(find_sum([1, 2, 3, 4], 5))
