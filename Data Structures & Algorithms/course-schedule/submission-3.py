from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list & in-degree array: O(V + E)
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # Queue all nodes with 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed = 0

        # Kahn's algorithm: O(V + E)
        while queue:
            node = queue.popleft()  # O(1) pop
            processed += 1

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If processed all vertices, graph is a DAG (no cycle)
        return processed == numCourses