class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = [0]*256  #array of curr values
        needed = [0]*256 #arr of required values 
        high=0
        low=0
        start = low #starting index of the valid substr
        res = float('inf')  #final len of valid substr
        required = len(t) #this tells us abt. how many char.still left 

        for c in t: #forming needed from str t                
            needed[ord(c)]+=1                    
        while high<len(s):
            #window formation
            have[ord(s[high])]+=1   #ord() returns ordinal val i.e, ASCII val for ASCII characters.
            if have[ord(s[high])]<= needed[ord(s[high])]: 
                required-=1
            #if have>needed then no need to do reqd-=1 bcz the requirement for this char is already satisfied.
            while required == 0:    # means no more char reqd Valid substr found 
                if (high-low+1) < res:  #currLen of crctsubst<res then update res
                    res=high-low+1
                    start=low
                have[ord(s[low])] -= 1
                if have[ord(s[low])]<needed[ord(s[low])]:   #invalid substr
                    required+=1
                low+=1
            high+=1
        if res==float('inf'):
            return ""
        return s[start:start+res]
