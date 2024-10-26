from typing import List
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v=len(graph)
        color=[-1]*v
        for i in range(v):
            if color[i]==-1:
                color[i]=0
                q=deque([i])
                while q:
                    u=q.popleft()
                    for n in graph[u]:
                        if color[n]==-1:
                            color[n]=1-color[u]
                            q.append(n)

                        elif color[u]==color[n]:
                            return False
        return True
        

s=Solution()
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))        
