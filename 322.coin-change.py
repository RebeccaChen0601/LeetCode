#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ### method 1

        # memo = {}
        # def dp(n):
        #     if n in memo: return memo[n]
        #     if n == 0: return 0
        #     if n < 0: return -1

        #     res = float('inf')

        #     for coin in coins:
        #         dp_res = dp(n - coin)
        #         if dp_res == -1: continue
        #         res = min(res, dp_res + 1)
            
        #     memo[n] = res if res != float('inf') else -1
        #     return memo[n]


        # return dp(amount)

        ### method 2

        dp = [amount + 1] * (amount + 1)  # 赋值最大值给不合适的以便于做min
        dp[0] = 0 #刚好凑齐整数给最小值0的base case
        
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i - coin]  + 1, dp[i])
        return dp[amount] if dp[amount] != amount + 1 else -1
 
                
# @lc code=end

