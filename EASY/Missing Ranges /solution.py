class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing=[]
        if len(nums)==0:
            missing.append([lower,upper])
            return missing

        if len(nums)==1:
            if lower<nums[0]:
                missing.append([lower,nums[0]-1])
            if nums[0]<upper:
                missing.append([nums[0]+1,upper])
            if lower==upper==nums[0]:
                return []
            return missing
            

        if lower < nums[0]:
            missing.append([lower,nums[0]-1])
        i=0
        for i in range(len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                missing.append([nums[i]+1,nums[i+1]-1])

        if (i+1)<len(nums) and nums[i+1] < upper:
            missing.append([nums[i+1]+1,upper])

        return missing
