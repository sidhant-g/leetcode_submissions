class Solution:
    def reorganizeString(self, s: str) -> str:
        n  = len(s)
        mp = defaultdict(int)
        heap = []   #max heap
        res = ""
        seat = 0
        for ch in s:
            mp[ch] +=1
        for ch, freq in mp.items():
            heapq.heappush(heap, (-freq, ch))
        while heap:
            p = heapq.heappop(heap)
            if seat == 0 or res[seat-1] != p[1]:
                res+= p[1]
                seat+=1
                p = (p[0]+1, p[1])
                if -(p[0]) > 0:
                    heapq.heappush(heap, p)
            else:       #seat > 0 and res[seat-1] == p[1]
                #now we need to select another char
                if not heap:    #heap empty ; cannot choose any other char
                    return ""
                #we can choose another char
                p2 = heapq.heappop(heap)
                res += p2[1]
                seat+=1
                p2 = (p2[0]+1, p2[1])
                if -(p2[0]) > 0:
                    heapq.heappush(heap, p2)
                heapq.heappush(heap, p)
        return res