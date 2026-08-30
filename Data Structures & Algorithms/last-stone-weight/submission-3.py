class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            x = max_heap[0]
            heapq.heappop(max_heap)
            y = max_heap[0]
            heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x-y)
            elif x > y:
                heapq.heappush(max_heap, y-x)

        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]
