class Solution:
    res = 0     # count the no of islands
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)   #total rows
        m = len(grid[0])    #total col
        i = 0
        j=0
        vis = [[0]*m for _ in range(0,n)]   #visited arr keeps tracks of which lands are already visited
        for i in range (0, n):  #iterate in row
            for j in range(0, m):   #iterate in col
                if grid[i][j]=='1' and vis[i][j] == 0:  #if land present and island not visited
                    self.dfs(grid, vis, i, j, n, m)
                    self.res+=1
        return self.res
    
    def dfs(self, grid: list[list[char]], vis: list[list[int]], i: int, j:int, n: int, m: int) -> None:
        vis[i][j] = 1   #as this land visited 
        #    up,down,left,right
        x = [-1, 1, 0, 0]   #for row-wise iteration
        y = [0, 0, -1, 1]   #for col-wise iteration
        for k in range(0, 4):   #4 bcz 4 directions t iterate for each node
            row = i+x[k]
            col = j+y[k]
            if self.valid(grid, row, col, n, m) and grid[row][col] == '1' and vis[row][col] == 0: #valid node, land present, not visited
                self.dfs(grid, vis, row, col, n, m)
        return None

    def valid(self, grid: list[list[char]], row: int, col: int, n: int, m: int)-> bool:
        if (row<0 or row>=n) or (col<0 or col>=m):  #total n valid rows exist from 0 to n-1 same for col.
            return False
        return True