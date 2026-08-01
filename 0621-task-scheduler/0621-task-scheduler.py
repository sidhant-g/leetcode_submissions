class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        heap = []
        for task in tasks:
            mp[task] +=1
        for task, freq in mp.items():
            heapq.heappush(heap, (-freq))
        time = 0    #CPU time = total tasks+idle time
        while heap:
            remain = []     #store the count of remaining tasks in this
            cycle = n+1     #single cycle is the main task + its cooldown period(given = n)
            while cycle and heap:
                max_freq = -heapq.heappop(heap)

                if max_freq > 1:    #instances of this task remaining
                    remain.append(-(max_freq - 1))
                
                time+=1     #task executed 
                cycle-=1    #one instanc of cycle used to execute the task

            #if tasks remaining then 
            #push them into heap for further execution
            for task in remain:
                heapq.heappush(heap, task)           
            
            #if no tasks remaining then
            #we don't need idle time so break early
            if not heap:
                break

            #in inner loop if heap becomes empty before cycle ends it means
            # we didn't have enough tasks to finish the cycle so we need idle time before next cycle begins
            time+=cycle     #whatever cycle is remaining is our idle time 
        
        return time 