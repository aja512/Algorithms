class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid = sum(cost) / 2
        count = 0
        for target, co in arr:
            count += co
            if count >= mid:
                return sum(abs(target - n) * c for n, c in arr)
