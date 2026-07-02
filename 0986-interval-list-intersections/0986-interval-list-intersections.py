class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res = []
        while i<len(firstList) and j< len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            if start1<=start2:  #sorted : firstList[start]<secondList[start]
                #merge logic 
                if end1>=start2:
                    s=max(start1,start2)
                    e=min(end1, end2)
                    res.append([s,e])
                #else no merge
            else: #start2<start1 ,  not sorted: firstList[start]>secondList[start]
                #merge logic reverse
                if end2>=start1:
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
                #else no merge
            if end1<=end2:  #firstList gets finished faster so update it
                i+=1
            else:   #end2<end1 ,  secondList gets finished faster so update it
                j+=1
        return res

