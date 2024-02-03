class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0 for i in range(W + 1)] for j in range(n)]
        
        for i in range(n):
            v = val[i]
            w = wt[i]
            
            for j in range(W+1):
                v1 = dp[i][j] = dp[i-1][j]
                if w > j:
                    dp[i][j] = v1
                else:
                    v2 = v
                    if j - w >= 0 and i > 0:
                        v2 += dp[i-1][j - w]

                    
                    dp[i][j] = max(v1, v2)
                    
        return dp[n-1][W]