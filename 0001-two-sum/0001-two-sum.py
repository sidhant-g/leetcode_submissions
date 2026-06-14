from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = 0
        map = defaultdict(int)
        while curr < len(nums):
            required = target - nums[curr]
            if required in map:
                return (map.get(required),curr)
            else:
                map[nums[curr]] = curr  
                curr+=1