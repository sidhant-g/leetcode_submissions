class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len (matrix)
        low = 0
        high = row -1
        col  = len(matrix[0])
        
        while low <= high:
            l = 0
            h = col-1
            mid = (low+high)//2
            
            if matrix [mid][l] > target:
                high = mid -1
            elif matrix[mid][h] < target:
                low = mid+1
            else:   #if the elem is present in matrix then it can be present only in this particular row 
                while l<=h:
                    m = (l+h)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m+1
                    else:   #matrix[mid][m] > target
                        h = m-1
                return False 
        return False    #eg: [[1]] high goes behind low in if condn so else: never executes 

                              