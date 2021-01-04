#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K+1) for _ in range(N+1)]
        for i in range(0, K+1):
            dp[0][i] = 0
        for i in range(1, N+1):
            dp[i][1] = i
        for i in range(1, N+1):
            for j in range(1, K+1):
                dp[i][j] = min([max(dp[I-1][j-1], dp[i-I][j]) for I in range(1, i + 1)]) + 1
        return dp[N][K]
# @lc code=end

