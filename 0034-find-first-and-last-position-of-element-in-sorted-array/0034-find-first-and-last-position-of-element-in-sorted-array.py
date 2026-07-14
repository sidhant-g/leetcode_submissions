class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def leftmost (nums: List[int], target: int) -> int:
            low = 0
            high = len(nums) -1
            leftmost = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] < target:
                    low = mid+1
                elif nums[mid]> target :
                    high = mid-1
                else:   #nums[mid] == target
                    leftmost = mid
                    high=mid-1  #to check if more leftmost targets possible
            return leftmost
        
        def rightmost (nums: List[int], target: int) -> int:
            low = 0
            high= len(nums) - 1
            rightmost = -1
            while low<=high:
                mid = (low+high)// 2
                if nums[mid] < target:
                    low = mid+1
                elif nums[mid] > target:
                    high =mid-1
                else:   #nums[mid] == target
                    rightmost = mid
                    low = mid+1 #to check if more rightmost targets possible
            return rightmost
        return [leftmost(nums, target), rightmost(nums, target)]