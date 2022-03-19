"""
LeetCode : 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
 LeetCode :
 34. Find First and Last Position of Element in Sorted Array
 

"""

def searchRange( nums: List[int], target: int) -> List[int]:
        
      start = 0
      end = len(nums) - 1

      index = -1
      # binary search algo to find any index of target number
      while start < end:

          mid = start + (end - start)//2
          if nums[mid] == target:
              index = mid
              break

          if target > nums[mid]:
              start = mid + 1
          else:
              end = mid - 1

      # special case handling when there is only 1 element in an array of 1 element
      if start == end and nums[start] == target:
          return [start, start]

      if index == -1:
          return [-1, -1]

      left = index
      right = index

      while left >=0 and nums[left] == target:
          left -= 1

      # if there is more than 1 element of same target value,  left would have moved else it wouldn't have
      if left != index:
          left += 1


      while right < len(nums) and nums[right] == target:
          right += 1

      # if there is more than 1 element of same target value,  right would have moved else it wouldn't have
      if right != index:
          right -= 1


      return [left, right]
            
