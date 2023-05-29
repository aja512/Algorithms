class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        return max(ceil(a / b) for a, b in zip(sorted(jobs), sorted(workers)))
