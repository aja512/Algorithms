class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if c & 1 == 0:
                res += (a & 1) + (b & 1)
            else:
                if a & 1 == 0 and b & 1 == 0:
                    res += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return res
