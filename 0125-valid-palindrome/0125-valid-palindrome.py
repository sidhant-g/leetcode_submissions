class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for c in s:
            if c.isalnum():
                clean_s += c.lower()
        low = 0
        high = len(clean_s) - 1

        return self.helper(clean_s, low, high)
        
    def helper(self, clean_s: str,low: int, high: int)->bool:
        if low >= high:
            return True
        if clean_s[low] != clean_s[high]:
            return False

        return self.helper(clean_s, low+1, high-1)
