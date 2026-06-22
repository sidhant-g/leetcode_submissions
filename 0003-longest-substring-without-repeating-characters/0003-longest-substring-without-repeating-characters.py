from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        low=0
        high=0
        res=0
        charMap=defaultdict(int)
        while high<n:
            charMap[s[high]]+=1
            if charMap[s[high]] <= 1:
                res = max(res, high-low+1)
                high+=1
            else:   #duplicate found
                while charMap[s[high]] > 1:
                    charMap[s[low]] -=1
                    if charMap[s[low]] == 0:
                        del charMap[s[low]]
                    low+=1
                high+=1
        return res
