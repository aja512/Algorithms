class Solution:
    def numberOfWays(self, s: str) -> int:
        one = zero = one_zero = zero_one = 0
        result = 0

        for char in s:
            if char == '0':
                zero += 1
                one_zero += one
                result += zero_one
            else:
                one += 1
                zero_one += zero
                result += one_zero
        
        return result
