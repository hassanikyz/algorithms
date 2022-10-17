
"""
Leetcode 78: Subsets
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subset = []

        #all subsets are created by either including an element from the list or not including it and looking at remaining ones 
        #in a similar fashion. You walkthrough entire list that way. The fact you repeat this procedure on 'remaining' ones means
        #you can use recursion.

        def helper(subset, pos):

            if pos >= len(nums):
                # if we have looked at the last element already, let's collect all subsets
                subsets.append(copy.copy(subset))
            else:   

                #include the first element into the subset
                subset.append(nums[pos])
                #call recursively using next position in the input array
                helper(subset, pos+1)
       

                #excluding the first element, let's collect subsets on remaining the remaining list
                # but for that we must pass it the original subset list not the modified one
                # hence remove the element from subset (essentially backtracking)
                subset.pop()  
                helper(subset, pos+1)


        helper(subset, 0)
        return subsets
