"""
33. Search in Rotated Sorted Array
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lennums = len(nums)
        if len(nums) == 0 or target < nums[0] and target > nums[lennums - 1]:
            return -1
        
        found = False
        start  = 0
        end  = lennums - 1
        
              
        while (start <= end):
            
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                
                if target >= nums[start] and target < nums[mid]:
                    
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                
                if target > nums[mid] and target <=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                
        return -1

        
