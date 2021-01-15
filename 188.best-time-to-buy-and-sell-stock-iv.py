#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # ## 自顶向下
        # n = len(prices)

        # @functools.cache
        # def dp(k, i, status):
        #     if k == 0 or i == n:
        #         return 0

        #     if status:    
        #         profit_sell = prices[i] + dp(k - 1, i + 1, status - 1) 
        #         profit_buy = float('-inf') 
        #     else:
        #         profit_sell = float('-inf') 
        #         profit_buy = dp(k, i + 1, status + 1) - prices[i]
            
        #     profit_wait = dp(k, i + 1, status)
           
        #     return max(profit_sell, profit_buy, profit_wait)
        # return dp(k, 0, 0)

        ## 自底向上
        n = len(prices)

        profit = [[0, -prices[0]] * n for _ in range(k)]

        for i in range(n):
            profit[0][i][1] = float('-inf') 

        for i in range(1, k):
            for j in range(1, n):
                profit[i - 1][j - 1][0] = max(prices[j] + profit[i - 1][j - 1][1], profit[i][j - 1][0])
                profit[i - 1][j - 1][1] = max(profit[i][j - 1][0] - prices[j],  profit[i][j - 1][1])
        
        return profit[k-1][n-1][0]


# @lc code=end

