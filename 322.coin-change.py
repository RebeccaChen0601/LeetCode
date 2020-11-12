#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1

            res = float('inf')

            for coin in coins:
                dp_res = dp(n - coin)
                if dp_res == -1: continue
                res = min(res, dp_res + 1)
            
            memo[n] = res if res != float('inf') else -1
            return memo[n]


        return dp(amount)
        
# @lc code=end

