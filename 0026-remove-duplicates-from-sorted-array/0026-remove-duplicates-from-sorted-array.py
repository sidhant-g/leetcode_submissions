class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        n = len(nums)
        for j in range(n):
            if i<1 or nums[j] != nums[i-1]: 
                nums[i] = nums[j]
                i+=1
        return i   