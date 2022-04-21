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


"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

# Solution # 2:
# ------------------------------------------------------------------ #
    def search( nums: List[int], target: int) -> int:
        
        # finding pivot through binary search method, faster than linear search performed in previous solution
        def find_pivot(left, right):
        
            
            if nums[right] > nums[left]:
                # if there is no rotation then left most element will be smaller than right most. 
                return 0
            else:
                # if there is rotation then lets search using the fact it was sorted to begin with.
                while left <= right:
                    pivot = (right + left)//2
                    
                    
                    if nums[pivot] > nums[pivot+1]:
                        # this can only happen if pivot + 1 element is smallest
                        return pivot + 1

                    if nums[pivot] < nums[left]:
                        # if pivot element is smaller than the leftmost it can only happen if situation is like this
                        #   [ 7, 8, 9, 0, 1, 2, 3, 4, 5, 6 ] 
                        #   pivot = 5th element => 2  which is smaller than leftmost 7
                        #   It means smallest element must be left side of the pivot.
                        #   so lets move the right pointer to left of the pivot
                        #   OR situation is like this
                        #   [ 4, 5, 1, 2, 3 ]  where 1 is the actual lowest element and is the pivoted one. Still we move right pointer to its left.
                        #   but will eventually exit via line # 87
                        right = pivot -1
                    else:
                        # if pivot element is greater than left element then scenario would be like this
                        #   [ 4, 5, 6, 7, 8, 9, 0, 1, 2, 3 ]
                        #   pivot = 5th element => 9 which is larger than 4
                        #   in this scenario most likely smallest element is on the right side of the pivot so move left pointer there.
                
                        left = pivot + 1
                    
            
        
        def bin_search(nums, target):
            
            start = 0
            end = len(nums) - 1
            while start <= end:
                
                mid = start + (end - start)//2
                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = start + 1
        
            return -1
        
        lennums = len(nums)
        if len(nums) == 0 or target < nums[0] and target > nums[lennums - 1]:
            return -1
        
        if lennums == 1:
            if target == nums[0]:
                return 0
            return -1
        
        
        # find the pivot
        lowest = find_pivot(0, lennums - 1)


        if target == nums[lowest]:
            return lowest
        
        if lowest == 0:
            return bin_search(nums, target)
        
        if target > nums[lowest] and target <= nums[lennums - 1]:
            index = bin_search(nums[lowest: ], target)
            if index == -1:
                return -1
            
            return lowest + index
        else:
            index = bin_search(nums[:lowest], target)
            if index == -1:
                return -1
            
            return index
 
        return -1
# ------------------------------------------------------------------ #
