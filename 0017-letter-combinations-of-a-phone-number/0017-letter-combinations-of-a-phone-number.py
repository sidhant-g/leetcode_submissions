class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        idx=0
        n = len(digits)
        res = []
        tmp = ""
        mp = defaultdict(str)
        mp['2'] = "abc"
        mp['3'] = "def"
        mp['4'] = "ghi"
        mp['5'] = "jkl"
        mp['6'] = "mno"
        mp['7'] = "pqrs"
        mp['8'] = "tuv"
        mp['9'] = "wxyz"

        self.helper(idx, tmp, n, res, mp, digits)
        return res
    
    def helper(self, idx: int, tmp: str, n: int, res: list[str],mp: defaultdict(str), digits: str) -> None:
        if idx == n:
            res.append(tmp)
            return
        choice = mp[digits[idx]]

        for j in range(0, len(choice)):
            tmp += choice[j]
            self.helper(idx+1, tmp, n, res, mp, digits)
            tmp = tmp[:-1]
        return  #func end so automatically returns