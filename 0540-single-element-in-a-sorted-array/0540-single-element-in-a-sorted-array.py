class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        if n==1:
            return nums[i]
        while i<n-1 :
            if nums[i]==nums[i+1]:
                i+=2
                if i==n-1:
                    return nums[i]
            else:      
                return nums[i]
        