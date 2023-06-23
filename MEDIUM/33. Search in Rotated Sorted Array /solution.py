class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        return self.modBS(nums, 0, n-1, n, target)
    
    def modBS(self, nums: List[int], left: int, right: int, n: int, target: int) -> int:
        
        if left > right or left < 0 or left >= n or right < 0 or right >= n:
            return -1
        
        mid = (left+right)//2
        
        current = nums[mid]
        
        if current == target:
            return mid
        
        if nums[left] <= current:
            
            if target >= nums[left] and target <= current:
                return self.modBS(nums, left, mid-1, n, target)
            else:
                return self.modBS(nums, mid+1, right, n, target)
        
        if target >= current and target <= nums[right]:
            return self.modBS(nums, mid+1, right, n, target)
        
        return self.modBS(nums, left, mid-1, n, target)

    
"""
[4,5,6,7,0,1,2]
 |     |     |
 0     3     6
"""
