class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        low = 0
        high = len(citations) - 1
        h=0     #no papers published and no citations received
        while low<= high :
            mid = (low+high) // 2
            paperPublished = n-mid  
            if citations[mid] >= paperPublished:
                h = paperPublished  #valid hIndex found
                high = mid -1
            else:
                low = mid+1     # not many citations received for papers published so reduce paperPublised
        return h