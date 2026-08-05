# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(0, len(lists)):  #store the head of each list in the heap
            if lists[i]:    #not empty list
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        dummy = ListNode(0)
        temp = dummy
        while heap:
            val, i, node = heapq.heappop(heap)  #storing i in case val of 2 elem equal then 
                                                #node comparision gives error so i is tie-breaker
            temp.next = node   
            temp = temp.next    #now temp points to the newly inserted node
            if node.next!= None:   #we insert (in heap) the next node of the node that we popped
                heapq.heappush(heap, (node.next.val, i, node.next)) # node was the elem that we popped from heap
        return dummy.next