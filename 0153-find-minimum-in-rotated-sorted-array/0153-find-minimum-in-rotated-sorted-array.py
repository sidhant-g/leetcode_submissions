class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high =n-1
        res = float('inf')
        while low<=high:
            mid  = (low+high) // 2
            if nums[mid] > nums[high]: # min on right half of mid
                res = min(res, nums[high])
                low = mid+1
            else:   # nums[mid] < nums[high] i.e, min on left half of mid
                res = min(res, nums[mid])
                high = mid -1
        return res    