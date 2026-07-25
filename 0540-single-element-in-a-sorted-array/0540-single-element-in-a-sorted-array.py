class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low<=high:
            mid = (low+high)//2
            if mid %2 != 0:
                mid-=1  
            #now mid is even 
            if mid+1< n and nums[mid] == nums[mid+1]:    #unique elem on right
                low = mid+2     #as nums[mid+1] would be duplicate
            else:   #unique elem on mid or left of mid
                matches_left =  mid>0 and nums[mid] == nums[mid-1]
                matches_right = mid+1 < n and nums[mid] == nums[mid+1]
                if not matches_left and not matches_right:  #unique elem found at mid
                    return nums[mid]
                high = mid-1    #unique elem surely on left of mid
        return -1 
