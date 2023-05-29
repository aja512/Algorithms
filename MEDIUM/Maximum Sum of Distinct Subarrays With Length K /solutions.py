class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        MaxSum = 0
        Sum = 0
        Cand = set()
        left = 0
        for i, num in enumerate(nums):
            if num in Cand:
                if nums[left] == num:
                    left += 1
                else:
                    Cand = set([num])
                    Sum = num
                    left = i
                continue
            Cand.add(num)
            Sum += num
            if len(Cand) == k:
                MaxSum = max(Sum, MaxSum)
                Sum -= nums[left]
                Cand.remove(nums[left])
                left += 1
        return MaxSum
