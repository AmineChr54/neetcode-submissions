class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
            
        parent = {i:i for i in range(n)} # each node is its own parent

        def union(u,v):
            parent[find(v)] = find(u)
        
        def find(u):
            cur = u
            while parent[cur] != cur:
                cur = parent[cur]
            return cur

        for u,v in edges:
            if find(v) == find(u):
                return False
            union(u,v)

        return True
                
