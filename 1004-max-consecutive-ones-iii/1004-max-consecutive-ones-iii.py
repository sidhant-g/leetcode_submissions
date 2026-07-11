class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        res=0
        n=len(nums)
        count=0

        while high<n:
            if nums[high]==1:
                count+=1        #keep the count of 1.

            zeroes = (high-low+1) - count     #number of elements that need to be modified.

            if zeroes<=k:     #valid window (The elements that need to be modified can be modified)
                res = max(res, (high-low+1))
                high+=1     #window expands
            else:   #invalid window(zeroes present in subarr cannot be exchanged with 1's)
                while zeroes > k:  #invalid window( elements that need to be modified can't be modiified)
                    low+=1
                    if nums[low-1]==1:
                        count-=1
                    zeroes = (high-low+1) - count

                high+=1     #now valid window So, window expand

        return res