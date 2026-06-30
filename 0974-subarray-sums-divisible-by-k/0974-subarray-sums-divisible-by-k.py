class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res = 0
        remainder = 0
        num_with_same_remainder = 0
        currsum = 0
        mp = defaultdict(int)
        mp[0] = 1
        for i in range(n):
            currsum+=nums[i]
            if nums[i]<0:
                remainder = -((abs(nums[i])%k))%k
            remainder = currsum % k
            num_with_same_remainder = mp[remainder]
            res+=num_with_same_remainder
            mp[remainder]+=1
        return res