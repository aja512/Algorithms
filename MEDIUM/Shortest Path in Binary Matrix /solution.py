from itertools import product
import heapq

class Solution:
    def shortestPathBinaryMatrix(self, A):
        #boundary case
        if A[0][0] or A[-1][-1]: return -1
        n = len(A)
        #heuristic function
        def h(x,y): return max(n-x, n-y)

        # direction
        direction = list(product([0,-1,1],[0,-1,1]))[1:] 
        heap = [[h(0,0), 0, 0]]
        heapq.heapify(heap)

        #distance map
        dmap = defaultdict(lambda: float("Inf"))
        dmap[0,0] = 1
        
        while heap:
            _, x, y = heapq.heappop(heap)
            d = dmap[x,y]
            # reach target
            if x==n-1 and y==n-1: return d
            #BFS
            for dx, dy in direction:
                xx, yy = x+dx, y+dy

                if xx<0 or yy<0 or xx>=n or yy>=n or A[xx][yy] == 1: continue
                if d+1<dmap[xx,yy]:
                    dmap[xx,yy] = d+1
                    heapq.heappush(heap, [d+h(xx,yy), xx, yy])

        return -1
