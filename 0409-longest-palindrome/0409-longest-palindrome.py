class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = defaultdict(int)
        res = 0 
        odd = False # assume no odd occurences of char present
        for i in s:
            mp[i] += 1
        for count in mp.values():   #mp.values() returns a dict view object
            #to make longest palindrome take all even occ + (odd occ-1) (make odd occ even) + take single odd for centre
            if count %2 ==0:    #even char
                res += count
            else:               #odd char
                res += count -1 #make odd occurences even 
                odd = True      #add the single leftout odd char at the centre of the palindrome
        if odd == True: #single odd char left
            res += 1    #the single odd char to keep at centre
        return res