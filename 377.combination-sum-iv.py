#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
           smalls = [x for x in nums if x <= target]
           dp[i] = sum(dp[i - x] for x in smalls)
        return dp[-1]

        
# @lc code=end

