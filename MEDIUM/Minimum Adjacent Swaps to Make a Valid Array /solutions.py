class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        m = min(nums)
        idx1 = nums.index(m)
        
        nums = [m] + nums[:idx1] + nums[idx1+1:]
        m = max(nums)
        idx2 = nums[::-1].index(m)
        
        return idx1 + idx2
