class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for i in range (0,k):
            heapq.heappush(heap, nums[i])
        for i in range(k, n):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]