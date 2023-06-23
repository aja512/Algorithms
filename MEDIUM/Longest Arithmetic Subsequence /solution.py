class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        num_range = max(nums) - min(nums)
        res = 2
        
        for abs_diff in range(num_range + 1):
            if abs_diff * (res - 1) >= num_range:
                break
            for diff in (-abs_diff, abs_diff):
                counter = defaultdict(lambda: 1)
                for num in nums:
                    prev_num = num - diff
                    if prev_num in counter:
                        counter[num] = max(counter[num], counter[prev_num] + 1)
                    res = max(res, counter[num])
        return res
