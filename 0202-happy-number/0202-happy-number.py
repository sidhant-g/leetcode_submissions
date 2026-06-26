class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        def numSquare (n: int)-> int:
            total=0
            while n>0:
                digit=n%10
                total+=(digit*digit)
                n=n//10
            return total
        while fast!=1:
            slow= numSquare(slow)
            fast = numSquare(fast)
            fast=numSquare(fast)
            if slow == fast and fast!=1:
                return False
        return True        