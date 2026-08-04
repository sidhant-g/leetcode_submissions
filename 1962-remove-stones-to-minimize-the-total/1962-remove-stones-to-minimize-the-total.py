
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        res = 0
        for i in range(0, len(piles)):
            heapq.heappush(heap, (-piles[i], i))
        while k!=0:
            p = heapq.heappop(heap)
            index = p[1]
            num = -p[0]
            piles[index] = ceil(num/2)
            heapq.heappush(heap, (-(piles[index]), index))
            k-=1
        for num in piles:
            res+=num
        return res