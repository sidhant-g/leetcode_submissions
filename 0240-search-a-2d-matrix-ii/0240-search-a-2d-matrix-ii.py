class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #total rows 
        m = len(matrix[0])  #total col
        row = n-1   #start from bottom left corner
        col = 0 
        while row>=0 and col < m:  #either rows or col empty
            if target < matrix[row][col]:
                row-=1              #eliminate rows 
            elif target > matrix[row][col]:
                col+=1              #eliminate columns
            else:   #target == matrix[row][col]
                return True
        return False 