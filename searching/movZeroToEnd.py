# Leetcode problem # 283
# https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        Algorithm
        
        Using 2-pointer approach, start both pointers from the beginning and locate 
        zero and nonzero numbers where nonzero pointer must be ahead of zero pointer. 
        Once such a sitation is encountered we swap numbers and increment both pointers 1 by 1
        until the nonzero pointer reaches the end of the list
        """  

        zero = 0
        nonzero = 0
        while nonzero < len(nums):
            
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            
            while nonzero < len(nums) and nums[nonzero] == 0:
                nonzero += 1

            if zero < nonzero and nonzero < len(nums) and zero < len(nums) and nums[zero] == 0 and nums[nonzero] != 0:
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                zero += 1

            nonzero += 1
            
            
            
