import java.lang.Math;

class Solution {
    public int numSquares(int n) {
        int n_sq = (int) Math.sqrt(n);
        int[][] dp = new int[n_sq+1][n+1];
        int[] squares = new int[n_sq+1];
        for (int i=1; i*i<=n; i++){
            squares[i] = i*i;
        }
        
        for (int i=0; i*i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if (i==0) {
                    dp[i][j] = j;
                }
                else{
                    dp[i][j] = dp[i-1][j];
                    if (j >= squares[i]) {
                        dp[i][j] = Math.min(dp[i][j], 1+ dp[i][j-squares[i]]);
                    }
                }
            }
        }
        return dp[n_sq][n];
    }
}