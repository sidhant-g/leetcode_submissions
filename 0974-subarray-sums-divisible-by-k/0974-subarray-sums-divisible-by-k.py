class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res = 0
        remainder = 0
        any_prefixsum_with_same_remainder = 0
        currsum = 0
        mp = defaultdict(int) #map keeps (remainder->count of that remainder in the subarray)
        mp[0] = 1
        for i in range(n):
            currsum+=nums[i]
            if currsum<0:
                remainder = (-(abs(currsum)%k)+k)%k #1st compute remainder as if its +ve ; make the remainder-ve; add k & again modulo with k
            else: 
                remainder = currsum % k
            any_prefixsum_with_same_remainder = mp[remainder] #this tells us if any prev prefix has same remainder if,yes; remove it and count of that remainder tell that how many subarr have that same remainder
            res+=any_prefixsum_with_same_remainder
            mp[remainder]+=1
        return res