class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0
        s = len(isConnected)
        seen = set()
        
        def dfs(p):
            for q, adj in enumerate(isConnected[p]):
                if (adj == 1) and (q not in seen):
                    seen.add(q)
                    dfs(q)
        
        count = 0
        for i in range(s):
            if i not in seen: 
                dfs(i)
                count += 1
        
        return count
