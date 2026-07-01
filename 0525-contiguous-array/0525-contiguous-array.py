class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        idx=0
        zeroes=0
        ones=0
        mp = defaultdict(list)
        for i in range(n):
            if nums[i]==0:
                zeroes+=1
            else:
                ones+=1
            diff = ones-zeroes  #gives extra number of ones in the curr subarr
            if diff not in mp:
                mp[diff] = i
            idx = mp[diff]  #tells the smallest ending index of any subarr(if present) with same number of extra ones
            if ones == zeroes:  #longest subarr found
                res = ones+zeroes
            res = max(res, i-idx)
        return res
