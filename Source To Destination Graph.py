from collections import deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        while q:
            checking_node = q.popleft()
            if checking_node == destination:
                return True
            for neighbor in adj[checking_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return False

solution = Solution()
n = 6
edges = [[0,1], [0,2], [3,5], [5,4], [4,3]]
source = 0
destination = 5

result = solution.validPath(n, edges, source, destination)
print(result)
