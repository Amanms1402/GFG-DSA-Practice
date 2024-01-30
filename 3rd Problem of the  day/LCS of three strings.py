class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        dp = [[[0 for k in range(n3+1)] for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                for k in range(n3+1):
                    if i == 0 or j == 0 or k == 0:
                        dp[i][j][k] = 0
                    elif A[i-1] == B[j-1] and A[i-1] == C[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1])
        return dp[n1][n2][n3]