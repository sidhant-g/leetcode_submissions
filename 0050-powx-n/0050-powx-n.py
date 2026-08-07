class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n<0:
            return 1 /self.myPow(x, -n)    #make n positive
        
        half = self.myPow(x, n//2)  #slice power in half
        
        if n%2 == 0:    #even power
            ans = half * half
        else:           #odd
            ans = half* half * x
        return ans