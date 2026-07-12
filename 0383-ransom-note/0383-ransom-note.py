class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = [0]*256
        need = [0]*256
        reqd = len(ransomNote)  # total len of required characters
        for i in ransomNote:
            need[ord(i)] += 1
        for ch in magazine:
            have[ord(ch)] += 1
            if have[ord(ch)] <= need[ord(ch)]:  #required char from ransomNote found
                reqd -= 1
            #else no need to update reqd as the requirement of that char is already satisfied
        if reqd == 0:
            return True
        return False