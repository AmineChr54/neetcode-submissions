class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set([i for i in range(n)])
        components = 0

        def bfs(cur):
            q = deque([cur])
            visited = {cur}
            while q:
                c = q.popleft()
                neighbors = []
                for e1, e2 in edges:
                    if e1 == c and e2 not in visited:
                        neighbors.append(e2)
                    elif e2 == c and e1 not in visited:
                        neighbors.append(e1)
                print("current: ", c, "neighbors:" ,neighbors)
                for neighbor in neighbors:
                    q.append(neighbor)
                    visited.add(neighbor)
                    nodes.remove(neighbor)

        while nodes:
            cur = nodes.pop()
            bfs(cur)
            components += 1

        return components