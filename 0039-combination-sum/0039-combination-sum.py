class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        idx = 0
        sum = 0
        n = len(candidates)

        self.helper(target, n, idx, tmp, sum, candidates, res)
        return res
    
    def helper(self, target: int, n: int, idx: int, tmp: list[int], sum: int, candidates: list[int], res: list[list[int]])-> None:
        if idx == n:
            if sum == target:
                res.append(tmp.copy())
            return
        
        self.helper(target, n, idx+1, tmp, sum, candidates, res)

        if (candidates[idx] + sum) <= target:
            sum += candidates[idx]
            tmp.append(candidates[idx])
            self.helper(target, n, idx, tmp, sum, candidates, res)
            tmp.pop()
            sum -= candidates[idx]
        return 