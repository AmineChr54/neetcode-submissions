class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x-y)

        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]
