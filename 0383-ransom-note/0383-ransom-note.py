class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = defaultdict(int)
        reqd = len(ransomNote)
        for i in ransomNote:
            mp[i] +=1
        for ch in magazine:
            if mp[ch] > 0:  # more ch char required
                reqd -= 1
                mp[ch] -= 1
        if reqd == 0:   #all required char present in magazine
            return True #contruction of ransomNote possible
        return False