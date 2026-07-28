from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        mp = defaultdict(int)
        heap = []
        res = []
        for num in nums:
            mp[num]+=1
        for num, freq in mp.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq,num))
                elif freq == heap[0][0]:
                    if num < heap[0][1]:    #smaller number get priority fot staying in min heap
                        heapq.heapreplace(heap, (freq,num))
                else:   #freq<heap[0][0]
                    continue
        for pair in heap:
            res.append(pair[1])
        return res
