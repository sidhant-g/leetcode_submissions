from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        low=0
        high=0
        resLen=0
        fruit_Map = defaultdict(int)
        while high<n:
            fruit_Map[fruits[high]]+=1
            if len(fruit_Map)<=2:
                resLen = max(resLen, high-low+1)
                high+=1
            else:   #invalid window
                while len(fruit_Map)>2:    
                    fruit_Map[fruits[low]] -= 1
                    if fruit_Map[fruits[low]]==0:
                        del fruit_Map[fruits[low]]
                    low+=1
                high+=1   
        return resLen