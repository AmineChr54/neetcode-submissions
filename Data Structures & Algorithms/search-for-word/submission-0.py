class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        initial_values = []
        
        m,n=len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    initial_values.append((i,j))
        def choice_is_valid(choice):
            return choice[0] < m and choice[0] >= 0 and choice[1] < n and choice[1] >= 0 and (choice[0],choice[1]) not in current_path
        
        def backtrack(i, j, i_word):
            if i_word == len(word)-1 and board[i][j] == word[-1]:
                self.result = True
                return

            choices = [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]

            for choice in choices:
                if self.result:
                    return 
                if choice_is_valid(choice) and board[choice[0]][choice[1]] == word[i_word + 1]:
                    current_path.append(choice)
                    backtrack(choice[0], choice[1], i_word + 1)
                    current_path.pop()

        self.result = False
        for i,j in initial_values:
            if self.result:
                break
            current_path = [(i,j)]
            backtrack(i,j, 0)

        return self.result