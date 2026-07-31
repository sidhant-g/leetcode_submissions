class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        heap = []
        for num in stones:
            heapq.heappush(heap,-num)
        if n == 1:
            return  -(heapq.heappop(heap)) 
        while heap:
            stone1 = -(heapq.heappop(heap))
            stone2 = -(heapq.heappop(heap))
            if stone1 < stone2:
                heapq.heappush(heap, -(stone2 - stone1))
            elif stone1 > stone2 :
                heapq.heappush(heap, -(stone1-stone2))
            if len(heap) == 1:
                return -(heapq.heappop(heap))
        return 0