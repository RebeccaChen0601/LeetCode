/*
 * @lc app=leetcode id=309 lang=java
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
 *
 * algorithms
 * Medium (43.64%)
 * Total Accepted:    86.2K
 * Total Submissions: 197.4K
 * Testcase Example:  '[1,2,3,0,2]'
 *
 * Say you have an array for which the i^th element is the price of a given
 * stock on day i.
 * 
 * Design an algorithm to find the maximum profit. You may complete as many
 * transactions as you like (ie, buy one and sell one share of the stock
 * multiple times) with the following restrictions:
 * 
 * 
 * You may not engage in multiple transactions at the same time (ie, you must
 * sell the stock before you buy again).
 * After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
 * day)
 * 
 * 
 * Example:
 * 
 * 
 * Input: [1,2,3,0,2]
 * Output: 3 
 * Explanation: transactions = [buy, sell, cooldown, buy, sell]
 * 
 */
class Solution {
    // dynamic programming tips:
    // 1. logic: save up to date the best path, compare it with the new operation
    // 2. classify operations into different possibilities: either sell, buy, hold.
    public int maxProfit(int[] prices) {
        if(prices.length == 0) return 0;
        int [] buy = new int[prices.length];
        int [] sell = new int[prices.length];
        buy[0] = 0 - prices[0];
        int prev = 0;
        for(int i = 1; i < prices.length; i++) {
            prev = i >= 2 ? sell[i - 2]:0;
            //prev: the day before yesterday's accumulated profit, since everytime you buy, there must be an hold day before it 
            buy[i] = Math.max(prev - prices[i], buy[i - 1]);
            sell[i] = Math.max(buy[i - 1] + prices[i], sell[i - 1]);
            // buy[i - 1]: (the day before yesterday's accumulated profit + new buy in yesterday) or hold yesterday
        }
        return sell[prices.length - 1];
    }
}

