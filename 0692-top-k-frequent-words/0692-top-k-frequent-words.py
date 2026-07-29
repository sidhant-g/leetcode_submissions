class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        mp = defaultdict(int)
        heap = []
        res = []
        for i in words:
            mp[i] +=1
        for word, freq in mp.items():
            if len(heap) < k:
                heapq.heappush(heap, Pair(freq, word))
            else:
                if heap[0] < Pair(freq,word):
                    heapq.heapreplace(heap, Pair(freq,word))
        while heap:
            res.append(heapq.heappop(heap).second)  #elem popped is in pair and we want the 1st of that popped elem
        res.reverse()   #res was made to be in ascending order
        return res

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        return self.second > other.second

        