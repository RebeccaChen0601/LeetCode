#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = f[i - 1][j] + f[i][(j - 1)]
        return f[-1][-1]
        
# @lc code=end

