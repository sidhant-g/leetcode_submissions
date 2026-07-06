class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [-1] * n
        stack = []
        mp = defaultdict(int)
        for i in range (0, 2*n):    #iterating in circular array; us len as 2*n and access idx using i%n
            while stack and nums[stack[-1]] < nums[i%n]:  #ith elem is greater
                res[stack[-1]] = nums[i%n]  
                stack.pop()
            stack.append(i%n)   #append indices when either stack empty or nums[i] <= nums(stack[-1])  
        return res