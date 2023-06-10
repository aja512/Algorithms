M = 10**9+7

@cache
def f(l, smn, smx):
    if smn > smx: return 0
    if smx == 0: return 1
    if smn > l * 9: return 0
    if smx > l * 9: return f(l, smn, l * 9)
    if l == 0: return int(smn <= 0 and smx >= 0)
    # if l == 1: return min(9, smx) - max(0, smn) + 1
    return sum(f(l-1, smn-x, smx-x) for x in range(min(9, smx)+1)) % M

def f2(n: str, smn, smx):
    l = len(n)
    res = 0
    for i, x in enumerate(map(int, n)):
        for y in range(x):
            res = (res + f(l-i-1, smn-y, smx-y)) % M
        smn -= x
        smx -= x
        if smx < 0: break
    # return (res + int(smn <= 0 and smx >= 0)) % M
    return res

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # n1 = str(int(num1) - 1)
        return (f2(num2, min_sum, max_sum) - f2(num1, min_sum, max_sum) + int(min_sum <= sum(map(int, num2)) <= max_sum)) % M
