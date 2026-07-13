class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low<= high :
            mid = (low+high) //2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:  #all the elem present before mid and mid itself are less than target
                low = mid+1
            else: # nums[mid] > target all the elem present after mid and mid itself are greater than target
                high = mid-1
        return -1