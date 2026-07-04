class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # stack creation
        stack.append(s[0])
        n= len(s)
        for char in s[1:n]:
            if not stack:   #to check if stack empty
                stack.append(char)
                continue
            top = stack[-1] #access the topmost element of stack
            if char == top :
                stack.pop() #removes the top of stack
            else:
                stack.append(char)
        return "".join(stack)