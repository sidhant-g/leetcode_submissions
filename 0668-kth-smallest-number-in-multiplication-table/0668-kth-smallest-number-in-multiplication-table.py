class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 1   # min elem
        high = m*n   # max elem
        res = 0
        while low<= high:
            mid = (low+ high )// 2
            ans = self.countSmallerOccurences( m, n, k, mid)
            if ans < k: # no enough smaller elem present for this mid 
                low = mid+1
            elif ans>= k:   #enough smaller elem present for curr mid 
                res  = mid
                high = mid-1   #maybe another mid possible where also k smaller elem possible
        return res

    def countSmallerOccurences (self, m: int, n: int, k: int, mid: int) -> int:
        row = m
        col = 1
        count = 0
        while row > 0 and col <=n :
            if row*col > mid:  #row eliminate
                row-=1
            elif row*col <= mid:
                count = count+ (row)
                col+=1
        return count