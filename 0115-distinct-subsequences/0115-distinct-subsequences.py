class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] will store the number of distinct subsequences of s that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty target string t can be formed in 1 way

        for i in range(1, m + 1):
            # Iterate backwards to use values from the previous state of s
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]