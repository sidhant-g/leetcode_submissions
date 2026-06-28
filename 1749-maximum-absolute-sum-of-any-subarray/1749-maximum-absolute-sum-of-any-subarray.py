class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        i=1
        maxSum = nums[0]
        minSum = nums[0]
        while i< n:
            #calc max and min sum for each elem
            maxSum = max(maxSum+nums[i], nums[i])
            minSum = min(minSum+nums[i], nums[i])
            #store the absolute maximum in res
            res = max(res, abs(maxSum), abs(minSum))
            i+=1
        return abs(res)