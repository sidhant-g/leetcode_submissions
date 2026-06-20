class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        j=i+1
        n=len(nums)
        if n==1:
            return nums[i]
        while i<n-1 and j<n:
            if nums[i]==nums[j]:
                i+=2
                j+=2
                if j==n:
                    return nums[n-1]
            else:
                return nums[i]
        