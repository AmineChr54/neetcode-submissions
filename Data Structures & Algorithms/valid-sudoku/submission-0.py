class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        grids = [[] for _ in range(3)]
        for i in range(9):
            rows.append(set())
            cols.append(set())

        for i in range(3):
            for j in range(3):
                grids[i].append(set())
        
        for i in range(9): # y 
            for j in range(9): # x
                n = board[i][j]
                if n != '.':
                    grid_x = j // 3
                    grid_y = i // 3
                    
                    if n in rows[i] or n in cols[j] or n in grids[grid_x][grid_y]:
                        return False
                    rows[i].add(n)
                    cols[j].add(n)
                    grids[grid_x][grid_y].add(n)
        return True
        