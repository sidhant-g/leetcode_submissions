class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for i in range(0, len(edges)):
            edge = edges[i]
            src = edge[0]
            dest = edge[1]
            adj[src].append(dest)
            adj[dest].append(src)
        res = []
        visited = [0] * n
        self.dfs(adj, source, res, visited)
        if visited[destination] == 1:
            return True
        return False 

    def dfs(self, adj: list[list[int]], node: int, res: list[int], visited: list[int])-> None:
        res.append(node)    #node is the vertex or the index of adjacency list
        visited[node] = 1
        for i in range(0, len(adj[node])):  #adj[node] is a list of all the vertices connected to the node(OR its neighbours).
            neigh = adj[node][i]            # iterate in the neighbours one by one   
            if visited[neigh] == 0:
                self.dfs(adj, neigh, res, visited)
        return None