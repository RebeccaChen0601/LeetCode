#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 自顶向下
        # memo = {}
        # def dfs(substring):
        #     if substring in memo: 
        #         return memo[substring]
        #     if len(substring) == 0: 
        #         return 1
        #     if substring[0] == '0':
        #         return 0
        #     if len(substring) == 1:
        #         return 1
        #     nd1, nd2 = dfs(substring[1:]), 0
        #     if int(substring[0:2]) < 27:
        #         nd2 = dfs(substring[2:])
        #     memo[substring] = nd1 + nd2
        #     return memo[substring] 
        # return dfs(s)

        # 自底向上
        if not s:
            return 0
        dp = [0 for x in range(len(s) + 1)] 
        dp[0] = 1 
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            if 9 < int(s[i -  2:i]) < 27:
                dp[i] += dp[i - 2]
            if 0 < int(s[i - 1: i]):
                dp[i] += dp[i - 1] 
        return dp[len(s)]
        
        
# @lc code=end

