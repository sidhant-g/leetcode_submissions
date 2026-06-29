class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total = nums[0]
        for num in nums[1:]:
            total+= num
        left = 0
        right=0
        i=1
        #edge case: if prefix==suffix at 0 index
        if total - nums[0] == left: #total-nums[0] is suffix for nums[0]
            return 0    #prefixsum == suffixsum at 0th index
        while i<n:
            left += nums[i-1]
            right = total-nums[i]-left
            if left == right:
                return i
            i+=1
        return -1 