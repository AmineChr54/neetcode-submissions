class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def bfs_and_fill(r: int, c: int):
            q = deque([(r, c)])
            grid[r][c] = '0'
            
            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    bfs_and_fill(i,j)

        return islands    
