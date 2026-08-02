class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []   #max heap 
        arr = []    #total avlbl projects list
        i = 0 
        n = len(profits)
        while i<n:
            arr.append((capital[i], profits[i]))
            i+=1
        arr.sort(key = lambda x:x[0])   #sort acc to capital required
        j = 0
        while k!=0 :    #total projects we need to choose
            while j< n:
                if arr[j][0] > w:  #not enough capital avlbl to execute this project
                    break
                heapq.heappush(heap, -(arr[j][1]))  #heap return the max profit of all the avlbl projects 
                j+=1
            if not heap:    #heap gives us the list of avlb project if heap empty it means no projects to execute
                return w    #not enough projects to execute means we can't execute project with our avlbl capital
            project = - heapq.heappop(heap)   # the max profit project         
            w += project
            k-=1            # 1 project executed
        return w