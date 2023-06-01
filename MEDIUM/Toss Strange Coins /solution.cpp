class Solution 
{ 
public:
double probabilityOfHeads(vector<double>& p, int t)
{
	double dp[1002]{1.0};
	for(const auto & p : p)
		for(int j{t}; j>=0; --j)
			dp[j] = (j ? p*dp[j-1] : 0) + (1.0-p)*dp[j];  
   return dp[t];
}
};
