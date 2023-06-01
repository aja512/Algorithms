/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var numberOfPaths = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const memo = Array(m).fill().map(() => Array(n).fill().map(() => Array(k).fill(0)));

    memo[0][0][grid[0][0]%k] = 1;
    let s = grid[0][0];
    for (let i = 1; i < m; i++) {
        s = (s + grid[i][0])%k;
        memo[i][0][s] = 1;
    }
    s = grid[0][0];
    for (let j = 1; j < n; j++) {
        s = (s + grid[0][j])%k;
        memo[0][j][s] = 1;
    }
    const mod = 10**9 + 7;
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            for (let p = 0; p < k; p++) {
                let sum = (p + grid[i][j])%k;
                memo[i][j][sum] = (memo[i][j][sum] + memo[i-1][j][p])%mod; 
                memo[i][j][sum] = (memo[i][j][sum] + memo[i][j-1][p])%mod;
            }
        }
    }
    // console.log(memo)
    return memo[m - 1][n - 1][0];
};
