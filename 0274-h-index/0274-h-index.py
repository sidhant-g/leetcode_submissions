class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        low = 0 #no citations received for any research paper
        high = max(citations)
        ans = 0
        while low <= high:
            guess = (low+high) // 2
            hIndexValid = self.fun(citations, guess)
            if hIndexValid: #valid hIndex
                ans = guess
                low = guess+1 #increase hIndex
            else:
                high = guess-1
        return ans
        
    def fun(self, citations: List[int], guess: int) -> bool:
        l = 0
        h = len(citations) - 1
        count = 0   #tells if our hIndex is valid or not
        while l<=h:
            mid = (l+h)//2
            if citations[mid] >= guess:
                count = len(citations) - mid
                h = mid-1
            else:   #citations[mid] < hIndex
                l = mid+1
        if count >= guess:
            return True
        return False