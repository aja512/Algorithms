class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            idx = n - i - 1
            print(idx)
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] +=1
                return digits

        # we're here because all digits are nine 
        return [1] + digits
