class Solution:
    #questions asks us to arrange all the elem in sorted order and then return the kth elem (therefore its kth smallest not kth)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) #total rows
        m = len(matrix[0])  #total col
        low = matrix[0][0]  #min elem
        high = matrix[n-1][m-1] #max elem
        guess = 0
        ans = 0
        res = guess
        while low <= high:  #binary searching
            guess = (low+high) // 2
            ans = self.fun(matrix, guess, n, m)  #how many elem less than guess are present in matrix(less bcz sorted matrix giv)
            if ans < k: # k tells how many elem are required 
                low = guess+1
            else:   #ans>=k
                res = guess #eventually res becomes the least matrix value that satisfies atleast k samller elem being present 
                high = guess-1
        return res
    def fun(self, matrix: List[List[int]], guess: int, n: int, m: int) -> int:
        row = n-1
        col = 0
        count = 0
        while row>= 0 and col <m:
            if matrix[row][col] <= guess:
                count =  count + (row+1)    # all elem of this col are less than guess
                col+=1
            else:   #matrix[row][col] > guess
                row-=1
        return count