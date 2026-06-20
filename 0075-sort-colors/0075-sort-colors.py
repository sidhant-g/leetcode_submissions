class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        low=0
        mid=0
        high = n-1
        while mid<=high:
            if nums[mid]==0:
                temp = nums[low]
                nums[low]=nums[mid]
                nums[mid]=temp
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:           #nums[mid]==2
                temp = nums[high]
                nums[high]=nums[mid]
                nums[mid]=temp
                high-=1
