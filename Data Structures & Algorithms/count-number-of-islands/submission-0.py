class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def bfs_and_fill(i,j):
            q = deque()
            q.append((i, j))
            grid[i][j] = '0'

            while q:
                cur_i, cur_j = q.popleft()
                directions = ((cur_i,cur_j+1),(cur_i+1,cur_j),(cur_i,cur_j-1),(cur_i-1,cur_j))
                for d_i, d_j in directions:
                    if 0 <= d_i < len(grid) and 0 <= d_j < len(grid[0]) and grid[d_i][d_j] == '1':
                        q.append((d_i, d_j))
                        grid[d_i][d_j] = '0'


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result += 1
                    bfs_and_fill(i,j)

        return result    
