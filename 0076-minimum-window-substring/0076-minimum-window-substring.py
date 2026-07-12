class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low = 0
        reqd = len(t)
        start = low
        res = float('inf')
        need = defaultdict(int) # maps char to their required occurences
#need tells us how many more char are required so when we add a char to our window simply decrement the count of that char and when we remove a char from our window increment the count of that char
        for i in t :
            need[i] += 1
        for high in range (0, len(s)):
            if need[s[high]] > 0:  # requirement of ch not currently fulfilled
                reqd -= 1
            need[s[high]] -= 1  #always do bcz it helps in window shrinking later
            while reqd == 0: # valid substr containing all reqd char found
                # as valid substr found so now we try to find the min valid substr
                if (high-low+1) < res: # store the len if curr valid substr len < old valid substr len
                    res = high -low+1
                    start = low
                #start window shrinking
                need[s[low]] +=1
                low+=1   # low char may or maynot be part of reqd char
                if need[s[low-1]] > 0: # s[low] is a reqd char
                    reqd+=1         # bcz we removed a reqd char
            high+=1
        if res == float('inf'):
            return ""
        return s[start: start+res]