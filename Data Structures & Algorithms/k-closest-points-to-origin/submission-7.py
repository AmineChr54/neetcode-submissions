import heapq
from typing import List


class Solution:

  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # Max-heap storing (-distance, [x, y])
    max_heap = []

    for x, y in points:
      dist = x**2 + y**2
      if len(max_heap) < k:
        heapq.heappush(max_heap, (-dist, [x, y]))
      elif -dist > max_heap[0][0]:  # dist < current max distance in heap
        heapq.heapreplace(max_heap, (-dist, [x, y]))

    return [point for _, point in max_heap]