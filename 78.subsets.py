#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset, index):
            res.append(list(subset))
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        backtrack([], 0)
        return res

# @lc code=end

