class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
        
        return all(find(i) == find(i+1) for i in range(n-1))
            
