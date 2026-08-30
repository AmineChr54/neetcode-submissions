class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]    
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        print(max_heap)

        while len(max_heap) >= 2:
            x = max_heap[0]
            y = max_heap[1] if len(max_heap) == 2 else min(max_heap[1], max_heap[2])
            heapq.heappop(max_heap)
            heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x-y)
            elif x > y:
                heapq.heappush(max_heap, y-x)

        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]
