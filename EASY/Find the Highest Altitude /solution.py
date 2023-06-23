class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = prev = n = 0
        for i in gain:
            n = prev + i
            prev = n
            maxi = max(maxi, n)
        return maxi
