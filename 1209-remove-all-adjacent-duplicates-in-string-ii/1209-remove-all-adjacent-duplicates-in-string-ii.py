class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(0, len(s)):
            if not stack or stack[-1][0] != s[i]:
                stack.append([s[i], 1]) #pair stack stores List of [char, count] as an element
            else:  #stack not empty and ( stack[-1][0] == s[i]and stack[-1][0] != k
                stack[-1][1] += 1
                if stack[-1][1] == k :  #k duplicates of s[i] found
                    stack.pop()
        return "".join(char*count for char, count in stack)
        """
        OR
        res = ""
        for i in stack:
            res += i[0] * i[1]
        return res
        
        """