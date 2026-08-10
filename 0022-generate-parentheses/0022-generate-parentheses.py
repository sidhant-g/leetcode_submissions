class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0
        tmp = ""
        res = []

        self.helper(open, close, n, tmp, res)
        return res
        
    def helper(self, open: int, close: int, n: int, tmp: str, res: list[str]) -> None:
        if open == n and close == n:
            res.append(tmp)
            return 
        #open brackets push
        if open<n:
            tmp+='('
            self.helper(open+1, close, n, tmp, res)
            tmp = tmp[:-1]
        #close brackets push
        if close <open:
            tmp+=')'
            self.helper(open, close+1, n, tmp, res)
            tmp = tmp[:-1]
        