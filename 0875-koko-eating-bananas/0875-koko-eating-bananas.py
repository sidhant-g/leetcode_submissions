class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1     #koko can eat minimum 1 banana
        high = float('-inf')    # max amount of bananas koko can eat is the max elem in the piles arr
        res = float('inf')  # stores the min amount of bananas koko can eat in order to eat all bananas in h hours
        for x in piles:
            if x > high:
                high = x
        while low<=high:
            guess = (low+high) // 2     #how many bananas koko eating rn 
            hours = self.validHours(piles, guess)
            if hours > h: #koko is very slow at eating ; she needs to eat more bananas
                low = guess+1   #whatever amount of bananas koko was eating increase it by 1 
           
            #koko eating very fast ; but we need min amount of bananas she must eat in order to finish all bananas in h hours
            else:   #hours<h    
                res = min(res, guess)   #she can eat these much bananas
                high = guess-1     #check if koko eat less banana then can she still finish all bananas in h hours    
        return res             
    
    def validHours(self, piles: List[int], guess: int)->int:
        hours = 0
        for i in piles:
            hours += i//guess
            if i%guess != 0:
                hours+=1
        return hours               