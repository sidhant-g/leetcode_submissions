class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for i in range (0,len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]: #only enter when stack not empty & temp[i] >st[top]elem
                res [stack[-1]] = i-stack[-1]   # len from stack[top] elem to the greater elem
                stack.pop()
            stack.append(i)  # stores i index when stack empty or  nums[i] <= temp[st[top]] elem  
        return res