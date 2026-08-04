
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        res = 0
        for i in range(0, len(piles)):
            heapq.heappush(heap, (-piles[i]))
        while k!=0:
            num = -heapq.heappop(heap)
            sliced_num = num - num//2
            heapq.heappush(heap, -(sliced_num))
            k-=1
        for num in heap:
            res+= -(num)
        return res