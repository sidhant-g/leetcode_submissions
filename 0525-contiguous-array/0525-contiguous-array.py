class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        idx=0
        zeroes=0
        ones=0
        mp = defaultdict(list)
        mp[0] = -1  #initialise hashmap with assumption that 0 found at -1 index.
        for i in range(n):
            if nums[i]==0:
                zeroes+=1
            else:
                ones+=1
            diff = ones-zeroes  #gives extra number of ones in the curr subarr
            if diff not in mp:
                mp[diff] = i
            idx = mp[diff]  #tells the smallest ending index of any subarr(if present) with same number of extra ones
            res = max(res, i-idx)   #i-idx gives len of valid subarr
        return res
