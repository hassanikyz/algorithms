"""
LeetCode 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""
    def findMin(self, nums: List[int]) -> int:
        
        start  = 0
        end = len(nums) - 1
        
        if nums[0] < nums[end]:
            #array is not rotated
            return nums[0]
        
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            fwd = (mid+1)%len(nums)
            back = (mid-1)%len(nums)
            if nums[mid] < nums[back] and nums[mid] < nums[fwd]:
                return nums[mid]
            
            if nums[mid] > nums[start] and nums[end] < nums[mid]:
                start = mid+1
              
            else:
                if nums[end] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
                
            
        return nums[end]
        
