class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        low = 0
        high = 0
        reqd = len(s1)
        mp =defaultdict(int)    # maps char to its required occurences
        for i in s1:
            mp[i]+=1
        
        for high in range (0,len(s2)):
            if mp[s2[high]] >0: #more of these char required for valid permutation
                reqd -=1
                if reqd == 0:   #valid permutation found
                    return True
            mp[s2[high]] -= 1   #as s[high] found so decrement count bcz now one less s[high] reqd
            while mp[s2[high]] < 0: # this char is not reqd in our substr -ve means it was not reqd still was added to substr
                mp[s2[low]] +=1     # as s[low] is being removed so now one more s[high] reqd
                if mp[s2[low]] > 0: #now we require it in our substr
                    reqd += 1
                low+=1
        return False