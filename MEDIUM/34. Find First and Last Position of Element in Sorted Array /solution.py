class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(nums, left, right, start = True):

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ind = mid
                    if start:
                        while ind >= 0 and nums[ind] == nums[mid]:
                            ind -= 1
                        return ind + 1
                    else:
                        while ind < len(nums) and nums[ind] == nums[mid]:
                            ind += 1
                        return ind - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        first = bs(nums, 0, len(nums) - 1, start = True)
        last = bs(nums, 0, len(nums) - 1, start = False)    

        return [first, last]
