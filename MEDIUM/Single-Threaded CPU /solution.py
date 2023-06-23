class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        orders = [(enq, pro, i) for i, (enq, pro) in enumerate(tasks)]
        orders.sort()
        heap = []
        idle_on = 0
        res = []
        
        for enq, pro, i in orders:
            while heap and idle_on < enq:
                pro_prev, i_prev, enq_prev = heapq.heappop(heap)
                idle_on = max(idle_on, enq_prev) + pro_prev
                res.append(i_prev)

            heapq.heappush(heap, (pro, i, enq))
        return res + [i for _, i, _ in sorted(heap)]
