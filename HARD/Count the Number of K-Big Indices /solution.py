class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        
        if len(nums) < k * 2 + 1:
            return 0
        
        heap1 = []
        heap2 = []
        
        for i in range(k):
            heapq.heappush(heap1, -nums[i])
            heapq.heappush(heap2, -nums[len(nums)-1-i])
            
            
        is_valid = [False for _ in range(len(nums))]
        
        for i in range(k, len(nums)-k):
            peak = -heap1[0]
            if nums[i] > peak:
                is_valid[i] = True
            else:
                heapq.heappop(heap1)
                heapq.heappush(heap1, -nums[i])
        
        res = 0
        for i in range(len(nums)-k-1, k-1, -1):
            peak = -heap2[0]
            if nums[i] > peak:
                if is_valid[i]:
                    res += 1
            else:
                heapq.heappop(heap2)
                heapq.heappush(heap2, -nums[i])
            
        return res
