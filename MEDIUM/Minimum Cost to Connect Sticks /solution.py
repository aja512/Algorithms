import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sum = 0
        heapify(sticks)
        while len(sticks) > 1:
            min1 = heappop(sticks)
            min2 = heappop(sticks)
            add = min1 + min2
            sum += add 
            heappush(sticks, add)
        return sum
