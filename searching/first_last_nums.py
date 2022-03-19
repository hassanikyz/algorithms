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
      while start < end:

          mid = start + (end - start)//2
          if nums[mid] == target:
              index = mid
              break

          if target > nums[mid]:
              start = mid + 1
          else:
              end = mid - 1


      if start == end and nums[start] == target:
          return [start, start]

      if index == -1:
          return [-1, -1]

      left = index
      right = index

      while left >=0 and nums[left] == target:
          left -= 1

      if left != index:
          left += 1


      while right < len(nums) and nums[right] == target:
          right += 1

      if right != index:
          right -= 1


      return [left, right]
            
