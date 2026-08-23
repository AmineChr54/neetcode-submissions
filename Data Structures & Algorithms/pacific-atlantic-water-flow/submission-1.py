class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(heights), len(heights[0])

        def bfs(r, c):
            found_pacific = False
            found_atlantic = False
            q = deque([(r, c)])
            visited = {(r,c)}
            while q and not (found_pacific and found_atlantic):
                r, c = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    n_r, n_c = r+dr, c+dc
                    if (
                        0 <= n_r < m
                        and 0 <= n_c < n
                        and (n_r, n_c) not in visited
                        and heights[r][c] >= heights[n_r][n_c]
                    ):
                        q.append((n_r, n_c))
                        visited.add((r+dr, c+dc))
                    if n_r == -1 or n_c == -1:
                        found_pacific = True
                    if n_r == m or n_c == n:
                        found_atlantic = True
            return found_pacific and found_atlantic

        result = []
        for r in range(m):
            for c in range(n):
                if bfs(r, c):
                    result.append([r, c])
        return result
