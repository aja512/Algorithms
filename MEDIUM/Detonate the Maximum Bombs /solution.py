class Solution:
    # Idea - connect bombs, find the largest path in graph using DFS 
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        if n == 1:
            return n 
        g = collections.defaultdict(list)
        bombsToTry = set()
        # N^2
        for i in range(n):
            for j in range(i+1,n):
                Xi,Yi,Ri = bombs[i]
                Xj,Yj,Rj = bombs[j]
                dist = (Xi-Xj)*(Xi-Xj)+(Yi-Yj)*(Yi-Yj)
                # If center of bomb[i] belongs to the range of bomb[j] => bomb[j] will detonate bomb[i]
                if dist <= Rj*Rj:
                    g[j].append(i)
                    if len(g[j]) == n-1:
                        return n
                # If center of bomb[j] belongs to the range of bomb[i] ==> bomb[i] will detonate bomb[j]
                if dist <= Ri*Ri:
                    g[i].append(j)
                    if len(g[i]) == n-1:
                        return n

        def dfs(bombID, visited):
            visited.add(bombID)
            for nei in g[bombID]:
                if nei not in visited:
                    dfs(nei,visited)

        # Find largest path - run DFS from each node that has potential to detonate others
        bombsToTry = set([i for i in range(n) if i in g])
        maxDetonated = 1
        for bombID in list(bombsToTry):
            if bombID in bombsToTry:
                visited = set()
                dfs(bombID,visited)
                detonated = len(visited)
                if detonated == n:
                    return n
                maxDetonated = max(maxDetonated,detonated)
                bombsToTry -= visited
        return maxDetonated
