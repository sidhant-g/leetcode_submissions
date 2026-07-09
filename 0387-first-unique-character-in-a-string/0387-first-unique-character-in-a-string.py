class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = defaultdict(int)
        for i in range(len(s)): # store the freq of each elem in hashmap
            mp[s[i]] += 1
        for i in range(0, len(s)):
            if mp[s[i]] == 1: # check the unique elem
                return i
        return -1 