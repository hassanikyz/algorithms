

"""
Leetcode.com problem # 198
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""

class Solution(object):
    def rob_iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
    """
    KEY IDEA behind this iterative solution
    Keep track of max profit from house robbing in a list indexed by house location
    0th location should contain profit from robbing house 0 and so on.
    Base cases are of course if list is of length 1 then answer is 0th location contains number from house 1
    if # of houses are 2 then max of either one
    if # of houses are 3 or more then for 3rd house (location # 2), must contain max of current + previous max (excluding immediately previous house) or one further down. 
    We accumulate max numbers in a dp list. This ensure consecutive last 2 entries (and one of them) have the real max (final answer). That is the reason we look for last 2 
    previous not only at final return but also during calcutions at every ith location.
    
    """
        size = len(nums)
        dp = [0]*(size+1)
        
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])
        
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, size):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3] | 0)
            
        return max(dp[size - 1], dp[size - 2])
   

    def rob_recursive(self, nums):     
        memo = {}
   
        """
        key idea: Identify that there is recurrence relationship here. Find the max between two options/
        
        Recurrence equation:
        x = find max result from array starting with 1st index (not 0th)
        y = get 0th index value + find max result from array starting with 2nd index 
        return max of x and y
        
        Terminating condition should be when length is 1 or 2. These are the base cases anyway.
        i-e what is the result when there are only 2 houses or just 1 house.
        """
        def get_max(slate, index):

            if len(slate) == 1:
                return slate[0]
            if len(slate) == 2:
                return max(slate[0], slate[1])
            x = 0
            y = 0

            if index not in memo:
                x = get_max(slate[1:], index+1 )

                y = slate[0] + get_max(slate[2:], index + 2)
                memo[index] = max(x, y)
            return memo[index]
        i = 0
        return get_max(nums, i)
