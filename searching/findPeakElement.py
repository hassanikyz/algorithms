"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""

def findPeakElement_recursive(nums: List[int]) -> int:

      def helper(nums, s, e):

          if e == s:
              return s
          m = int(s  + (e - s)/2)            
          if nums[m] > nums[m+1]  :

              return helper(nums, s, m)

          return helper(nums, m+1, e)           

      return helper(nums, 0, len(nums) - 1)

# binary search in a different 


      
# This iterative solution is originally done by myself, above one (recursive) is taken from leetcode solution
def findPeakElement( nums: List[int]) -> int:
        
      lennums = len(nums)
      if lennums < 2:
          return 0

      left = 0
      right = len(nums) - 1

      while (left <= right):

          fwd = (left + 1) % lennums
          back = (left - 1) % lennums

          if   nums[back] < nums[left] > nums[fwd]:
              return left

          fwd = (right + 1) % lennums
          back = (right - 1) % lennums
          if  nums[back] < nums[right] > nums[fwd]:
              return right

          left += 1
          right -= 1

      return 0


"""
Binary search approach is usually applicable to sorted data for faster searching. 
In this case, we can go to mid every time and check mid and mid + 1 elements.
If mid element is smaller that means we can move the 'start' pointer to mid+1
If mid element is larger than next that means we could potentially have that element mid element as the peak 
hence we move the 'end' pointer to mid.

As result when start meets the end pointer we will be sure element pointed to by start is a peak element
"""

def findPeakElement_simple_bin_search( nums: List[int]) -> int:
      start  = 0
      end = len(nums) - 1

      while (start < end):

            mid = start + (end - start)//2
            if nums[mid] <  nums[mid + 1]:
                start = mid + 1
            else:
                end = mid

      return start
