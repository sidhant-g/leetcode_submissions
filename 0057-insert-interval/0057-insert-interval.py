class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        n=len(intervals)
        merge_list=[]
        insert = False #Flag to avoid multiple insertion of newinterval
        for i in range(n):
            if intervals[i][0]>=newInterval[0] and insert==False :
                merge_list.append(newInterval)
                merge_list.append(intervals[i])
                insert = True
            else:
                merge_list.append(intervals[i])
        if insert == False:
            merge_list.append(newInterval)
        
        result = self.merge(merge_list)
        return result

    def merge(self, merge_list: List[List[int]])->List[List[int]]:
            start1 = merge_list[0][0]
            end1 = merge_list[0][1]
            ans = []
            for i in range(1, len(merge_list)):
                start2  = merge_list[i][0]
                end2 = merge_list[i][1]
                if end1>=start2:
                    start1 = start1
                    end1 = max(end1, end2)
                    # no append here bcz we still don't know if this is the final interval eg; [[1,6], [1,8]]
                else:
                    ans.append([start1, end1])  #only append when finalized that no further merging possible
                    start1 = start2
                    end1 = end2
            ans.append([start1,end1])   #at the end(n-1) we still have an element left
            return ans
        
            

       
                    