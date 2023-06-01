class Solution {
        static final int mod = (int)1e9 + 7;
        public int numberOfPaths(int[][] a, int k) { 
            int m = a.length, n = a[0].length;
            int [][][] f = new int [m+1][n+1][k];
            f[0][1][0] = 1; 
            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++)
                    for (int v = 0; v < k; v++) 
                        f[i+1][j+1][(v + a[i][j]) % k] = (f[i+1][j][v] + f[i][j+1][v]) % mod;
            return f[m][n][0];
        }
}
