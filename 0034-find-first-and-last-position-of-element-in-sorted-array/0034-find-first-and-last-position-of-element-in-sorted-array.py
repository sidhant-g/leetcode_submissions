class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) -1
        while low<=high:
            mid  = (low+high) // 2
            if nums[mid] == target:
                while nums[low]!= target:
                    low+=1
                while nums[high]!=target:
                    high-=1
                return [low,high]
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return [-1,-1]