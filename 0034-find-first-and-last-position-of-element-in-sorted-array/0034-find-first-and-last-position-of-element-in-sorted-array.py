class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        firstOccurence  = self.firstOccurence(nums, target)
        lastOccurence = self.lastOccurence(nums, target)
        return [firstOccurence, lastOccurence]

    def firstOccurence (self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        firstOccurence = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] < target:
               low = mid+1
            elif nums[mid]> target :
                high = mid-1
            else:   #nums[mid] == target
                firstOccurence = mid
                high=mid-1  #to check if more firstOccurence targets possible
        return firstOccurence
        
    def lastOccurence (self, nums: List[int], target: int) -> int:
        low = 0
        high= len(nums) - 1
        lastOccurence = -1
        while low<=high:
            mid = (low+high)// 2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high =mid-1
            else:   #nums[mid] == target
                lastOccurence = mid
                low = mid+1 #to check if more lastOccurence targets possible
        return lastOccurence