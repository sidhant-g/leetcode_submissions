class Solution:
    def isValid(self, s: str) -> bool:
        n= len(s)
        stack = []
        for char in s:
            if not stack:   #if stack empty but string iteration not finished yet then; append the char.
                stack.append(char)
                continue
            top = stack[-1]
            if char==')' and top == '(':
                stack.pop()
                continue
            if char=='}' and top == '{':
                stack.pop()
                continue
            if char==']' and top == '[':
                stack.pop()
                continue
            stack.append(char)
        if not stack:   #stack=empty means all brackets in correct order
            return True
        return False    #if stack not empty; then not correct order or not enough correct brackets
