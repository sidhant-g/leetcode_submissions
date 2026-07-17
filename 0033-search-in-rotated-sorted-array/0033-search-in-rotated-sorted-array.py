class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = len(nums)-1
        if len(nums) == 1 :
            if nums[0] == target:
                return 0
            return -1
        while low <= high:
            mid = (low+high) // 2
            #we find min of rotated sorted arr & divide the arr in 2 parts
            if nums[mid] > nums[n-1]:   # min at right side of mid elem
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    low = mid+1
                else:   #target<nums[mid]
                    if target>=nums[0]:
                        high = mid-1
                    else:
                        low = mid+1
            else:  #nums[mid] < nums][n-1]  # min at mid or left of mid
                if target  == nums[mid]:    # eg: [6,7,0,1,2,4,5]
                    return mid
                elif target < nums[mid] : 
                    high = mid- 1
                else:   #target > nums[mid]
                    if target <= nums[n-1]:  
                        low =mid+1
                    else: 
                        high = mid -1
        return -1 