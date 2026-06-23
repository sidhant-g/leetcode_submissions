class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n= len(s)
        low=0
        high=0
        freaks=defaultdict(int)
        mostFreqVal = 0
        res=0
        while high<n:
            freaks[s[high]]+=1
            mostFreqVal = max(mostFreqVal, freaks[s[high]])
            charReplace = (high-low+1) - mostFreqVal
            if charReplace <= k:
                res=max(res, high-low+1)
                high+=1
            else:
                while charReplace > k:
                    freaks[s[low]]-=1
                    if freaks[s[low]] == 0:
                        del freaks[s[low]]
                    low+=1
                    charReplace  = (high-low+1)-mostFreqVal
                high+=1 
        return res



