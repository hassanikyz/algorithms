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
        
        
## ----------- another implementation --------------------- ##        
def findMin_sortedList(self, nums: List[int]) -> int:

    def search_min(left, right):

        if  nums[right] > nums[left]:
            return nums[left]

        while left <= right:

            pivot = (left + right)//2
            if nums[pivot] > nums[pivot+1]:
                return nums[pivot + 1]

            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1

    start = 0
    end = len(nums) - 1

    if nums[start] < nums[end] or end == 0:
        #array is not rotated
        return nums[0]

    return search_min(start, end)





