from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        currsum=0
        removesubarr_sum = 0
        res=0
        mp = defaultdict(int)
        mp[0]= 1
        for i in range(n):
            currsum+=nums[i]    
            removesubarr_sum = currsum-k    #the sum of subarr that need to be chopped off from currsum to make k
            subarr_toberemoved  = mp[removesubarr_sum] #count/value gives the total no of subarr that can be removed
            res+=subarr_toberemoved  #res give us the total number of removable subarr. 
            mp[currsum]+=1  #we have seen this currsum once so update inside map
        return res