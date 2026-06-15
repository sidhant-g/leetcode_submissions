class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        n = len(nums)
        while i<n-1 and j<n:
            if nums[j] != nums[j-1]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1  #i keeps the count of unique element +1 bcz nums is 0 indexed.