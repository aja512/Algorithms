class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if target <= nums[start]:
            return start
        elif nums[end] < target:
            return end + 1
        else:
            return end
