class Solution {
public:
    int MOD = 1e9 + 7;
    
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int dp[m][n][k+1];

        for(int i = 0; i<m; i++) {
            for(int j = 0; j<n; j++) {
                for(int r=0; r<k+1; r++) {
                    dp[i][j][r] = 0;
                }
            }
        }
        
        // base case
        int lastCellRemainder = grid[m-1][n-1] % k;
        dp[m-1][n-1][lastCellRemainder] = 1;
		
        int lastRemainder = lastCellRemainder;
        // last row base case
        for (int c = n-2; c >= 0; c--) {
            int cellRemainder = grid[m-1][c] % k;
            dp[m-1][c][(lastRemainder + cellRemainder) % k] = 1;
            lastRemainder = (lastRemainder + cellRemainder) % k;
        }
        
        lastRemainder = lastCellRemainder;
        // last col base case
        for (int r = m-2; r >= 0; r--) {
            int cellRemainder = grid[r][n-1] % k;
            dp[r][n-1][(lastRemainder + cellRemainder) % k] = 1;
            lastRemainder = (lastRemainder + cellRemainder) % k;
        }
        
        // Recurrence relation
        for (int r = m-2; r >= 0; r--) {
            for (int c = n-2; c >= 0; c--) {
                int cellRemainder = grid[r][c] % k;
                
                for (int rem = 0; rem < k; rem++) {
                    dp[r][c][(cellRemainder + rem) % k] = (dp[r][c][(cellRemainder + rem) % k] + dp[r][c+1][rem]) % MOD;
                    dp[r][c][(cellRemainder + rem) % k] = (dp[r][c][(cellRemainder + rem) % k] + dp[r+1][c][rem]) % MOD;
                }
            }
        }
        
        return dp[0][0][0];
    }
};
