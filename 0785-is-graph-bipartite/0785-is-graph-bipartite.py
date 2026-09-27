class Solution:
    res = True
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len (graph)
        colour = [-1] * n
        for i in range (0, n):  #ensuring broken graphs are also implemented
            if colour[i] == -1: #if current node not coloured call dfs()
                self.dfs(graph, colour, i, 0)
        return self.res

    def dfs(self, graph: list[list[int]], colour: list[int], node: int, c: int)-> None:
        colour[node] = c    #assign the colour to node and save it in the list
        for j in range(0, len(graph[node])):    #finding neighbours 
            neigh = graph[node][j]
            if colour[neigh] != -1 and colour[neigh] == c:  #if neigh coloured and same colour as our node
                self.res = False
            elif colour[neigh] == -1:   #if neigh still not coloured
                self.dfs(graph, colour, neigh, 1-c) # o and 1 are the colours
            #3rd case: neigh coloured with diff colour this means dfs already implemented for that node dats why its coloured
        return None