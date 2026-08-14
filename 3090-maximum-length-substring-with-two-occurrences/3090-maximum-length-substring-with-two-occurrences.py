class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        low = 0
        high = 0
        curr_len = 0
        res = 0
        while high<len(s):
            mp[s[high]] += 1
            while mp[s[high]] > 2:
                mp[s[low]] -=1
                if mp[s[low]] == 0:
                    del mp[s[low]]
                low+=1
            curr_len = high - low+1
            res = max(res, curr_len)
            high += 1
        return res