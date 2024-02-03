from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * len(adj)
        for i in range(len(adj)):
            if visited[i] == False:
                if self.DfsRec(adj, i, visited, -1):
                    return True
        return False

    def DfsRec(self, adj, s, visited, parent):
        visited[s] = True
        for u in adj[s]:
            if visited[u] == False:
                if self.DfsRec(adj, u, visited, s):
                    return True
            elif u != parent:
                return True
        return False