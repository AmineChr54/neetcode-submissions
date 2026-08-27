class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # A tree with n nodes MUST have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(u: int) -> int:
            if parent[u] != u:
                parent[u] = find(parent[u])  # Path compression
            return parent[u]

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False  # Cycle detected
            parent[root_v] = root_u

        return True