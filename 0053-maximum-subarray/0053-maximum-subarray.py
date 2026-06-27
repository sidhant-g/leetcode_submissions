class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        prev=0
        i=0
        best=float('-inf')
        res=float('-inf')
        while i<n:
            prev=best+nums[i]
            best=max(prev,nums[i])
            res=max(res,best)
            i+=1
        return res