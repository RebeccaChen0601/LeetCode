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
            if index == len(nums) + 1:
                return
            res.append(list(subset))
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        backtrack([], 0)
        return res

# @lc code=end

