class Solution(object):
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers)-1
        sum = 0
        while low<high:
            sum = numbers[low]+numbers[high]
            if sum == target:
                return[low+1,high+1]
            elif sum < target:
                low += 1
            else:           #sum > target
                high -=1
        