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
                    if (
                        0 <= r + dr < m
                        and 0 <= c + dc < n
                        and (r + dr, c + dc) not in visited
                        and heights[r][c] >= heights[r + dr][c + dc]
                    ):
                        q.append((r + dr, c + dc))
                        visited.add((r+dr, c+dc))
                    if r + dr == -1 or c + dc == -1:
                        found_pacific = True
                    if r + dr == m or c + dc == n:
                        found_atlantic = True
            return found_pacific and found_atlantic

        result = []
        for r in range(m):
            for c in range(n):
                if bfs(r, c):
                    result.append([r, c])
        return result
