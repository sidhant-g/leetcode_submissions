class Solution:
    def solve(self, board: list[list[str]]) -> None:
        x = [-1,1,0,0]
        y  = [0,0,-1,1]
        n = len(board)
        m = len(board[0])
        for i in range (0, n):
            if board[i][0] == "O":      #1st col 
                self.dfs(board, x, y, i, 0, n, m)
            if board[i][m-1] == "O":    #last col
                self.dfs(board, x, y, i, m-1, n, m)
        for j in range(0, m):
            if board[0][j] == "O":      #1st row
                self.dfs (board, x, y, 0, j, n, m)
            if board[n-1][j] == "O":    # last row
                self.dfs(board, x, y, n-1, j, n , m)
        for i in range(0, n):           #after dfs execution convert all edge and connected 0's to 0 from #  &  other 0 to X
            for j in range(0, m):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return None
    
    def dfs(self, board: list[list[str]], x: list[int], y: list[int], row: int, col: int, n:int, m: int) -> None:
        board[row][col] = "#"   #this 0 is either at edge or connected to edge
        for k in range(0, 4):   # iterate all 4 drcns for this 0 
            r = row+ x[k]
            c = col + y[k]
            if self.valid(board, n, m, r, c) and board[r][c] == "O":
                self.dfs(board, x, y, r, c, n, m)

    def valid(self, board: list[list[str]], n: int, m: int, r: int, c: int)-> bool:     # CHECK if valid iteration or not
        if (r< 0 or r>=n) or (c<0 or c>=m):
            return False
        return True