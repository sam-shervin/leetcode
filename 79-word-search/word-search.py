class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, ind):
            if ind == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[ind]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r-1, c, ind+1) or
                     dfs(r+1, c, ind+1) or
                     dfs(r, c-1, ind+1) or
                     dfs(r, c+1, ind+1))

            # backtrack
            board[r][c] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
