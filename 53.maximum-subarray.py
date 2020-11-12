#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')] * len(nums)
        res = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):  
            # print(i)
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            res = max(res, dp[i])

           
        return res
        
# @lc code=end

