
"""
Leetcode Problem https://leetcode.com/problems/house-robber-ii/ 
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
   """
      KEY IDEA 
    Keep track of max profit from house robbing in a list indexed by house location
    0th location should contain profit from robbing house 0 and so on.
    Base cases are of course if list is of length 1 then answer is 0th location contains number from house 1
    if # of houses are 2 then max of either one
    if # of houses are 3 or more then for 3rd house (location # 2), must contain max of current + previous max (excluding immediately previous house or one further down). 
    We accumulate max numbers in a dp list. This ensure consecutive last 2 entries (and one of them) have the real max (final answer). That is the reason we look for last 2 
    previous not only at final return but also during calcutions at every ith location.
   """
        
        def get_max(slate):
            size = len(slate)


            dp=[0]*(size + 1)

            if size == 0:
                return 0
            if size == 1:
                return slate[0]
            if size == 2:
                return max(slate[0], slate[1])
            
            dp[0] = slate[0]
            dp[1] = slate[1]
            for i in range(2, size):
                dp[i] = slate[i] + max(dp[i-2], dp[i-3]|0)

            
            return max(dp[size-1], dp[size-2])
        
        if len(nums) == 0:
                return 0
        if len(nums) == 1:
                return nums[0]
        
        # since homes are in a circular way, first house is connected to last
        # we need to elimnate 1st house once and last house in another attempt. Thus 
        # we are saying we need to find max between these two configurations 
        
        return max(get_max(nums[1:]), get_max(nums[:-1]))
