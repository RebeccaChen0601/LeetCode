#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        for k in range(1, ceil(((2 * N + 0.25) ** 0.5 - 0.5) + 1)):
            N -= k
            if N % k == 0:
                count += 1 
        return count
# @lc code=end

