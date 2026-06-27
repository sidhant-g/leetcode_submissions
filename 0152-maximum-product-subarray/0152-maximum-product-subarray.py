class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        maxEnding=nums[0]
        minEnding=nums[0]
        i=1
        while i < n:
            #i'th num can have 3 possibilities
            a1 = nums[i]
            a2 = maxEnding*nums[i] 
            a3 = minEnding*nums[i]
            maxEnding=max(a1,a2,a3) #store the max for next iteration
            minEnding = min(a1,a2,a3)   #store the min for next iteration
            res=max(res, maxEnding,minEnding)   #store the max in res using prev res and max for i'th num
            i+=1
        return res