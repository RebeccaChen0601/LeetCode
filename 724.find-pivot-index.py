#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == nums_sum - x - left_sum:
                return i
            left_sum += x 

        return -1
        
# @lc code=end


