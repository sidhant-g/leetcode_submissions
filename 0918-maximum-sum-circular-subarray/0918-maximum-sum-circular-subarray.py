class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        maxres=nums[0]
        minres = nums[0]
        i=1
        total = nums[0]
        maxSum = nums[0]
        minSum = nums[0]
        while i < n:
            #the max sum can either come from middle of the arr i.e simple maxSum
            maxSum = max(maxSum+nums[i], nums[i])
            #OR from both the ends combined; in this case minSum is present in the middle
            minSum = min(minSum+nums[i], nums[i])
            total += nums[i]
            maxres = max(maxres, maxSum)
            minres = min(minres, minSum)
            i+=1
        if maxres<0:    #all negative elements array
            return maxres   #otherwise minres==whole array & total-minres==0
        return max(maxres, total-minres)