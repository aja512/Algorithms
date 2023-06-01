class Solution {

    public double probabilityOfHeads(double[] prob, int target) {
        double[] dp = new double[target+1];
        dp[0] = 1.0;

        for (int i = 0; i < prob.length; i++) {
            for (int j = Math.min(i+1, target); j > 0; j--) {
                dp[j] = prob[i] * dp[j-1] + (1-prob[i]) * dp[j];
            }  
            dp[0] = (1 - prob[i]) * dp[0];
        }

        return dp[target];    
    }
}
