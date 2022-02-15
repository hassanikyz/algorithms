


"""
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
            
        # print(dp)
        return max(dp[size - 1], dp[size - 2])
   

    def rob_recursive(self, nums):     
        memo = {}
   
        """
        key idea: find the max from shorter and shorter lists from two different paths e.g 
        starting from 1st element and 2nd element. Find the max between two options
        1st and 0th + 2nd onwards.
        
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
