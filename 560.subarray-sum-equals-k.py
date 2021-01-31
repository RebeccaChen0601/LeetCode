#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        prefix_sum[0] = 1
        current_sum, count = 0, 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1
        return count

# @lc code=end
# 1, 1, 1     k = 2

