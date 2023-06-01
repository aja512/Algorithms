class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])


        # we store the numbers which are divisible by k on index 0
        dp = [[[0] * k for _ in range(col)] for _ in range(row)]
        rem = grid[0][0] % k
        dp[0][0][rem] = 1

        for r in range(1, row):
            dp[r][0][(rem + grid[r][0]) % k] = 1
            rem = (rem + grid[r][0]) % k

        rem = grid[0][0] % k
        for c in range(1, col):
            dp[0][c][(rem + grid[0][c]) % k] = 1
            rem = (rem + grid[0][c]) % k

        for r in range(1, row):
            for c in range(1, col):
                for rem in range(k):
                    dp[r][c][(rem + grid[r][c]) % k] = dp[r-1][c][rem] + dp[r][c-1][rem]

        return dp[-1][-1][0] % (10**9 + 7)
