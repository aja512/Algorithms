class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])
        mp = {}
        pq = [(0, s, 0)]
    
        while pq:
            total, cur, hop = heapq.heappop(pq)
            if cur == d:
                return total
            if cur in mp and mp[cur] <= hop:
                continue
            mp[cur] = hop
            for ne, w in graph[cur]:
                if ne not in mp or mp[ne] > hop:
                    heapq.heappush(pq, (w + total, ne, hop))
                if hop < k and (ne not in mp or mp[ne] > hop + 1):
                    heapq.heappush(pq, (total, ne, hop + 1))
        return -1
            
            
        
