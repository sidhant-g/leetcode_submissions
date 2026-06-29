from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        currsum=0
        diff = 0
        res=0
        mp = defaultdict(int)
        mp[0]= 1
        for i in range(n):
            currsum+=nums[i]    
            diff = currsum-k    #diff tells the sum of subarr that need to be chopped off from currsum to make k
            waystoremove_diff  = mp[diff] #count/value of the diff tells us how many ways in which we can remove the subarr with sum 'diff' i.e, it tells us the total removable subarr for particular i.
            res+=waystoremove_diff  #res give us the total number of removable subarr. 
            mp[currsum]+=1  #update map with 
        return res