 #
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.dfs(nums, 0, len(nums))
        return self.result

    def dfs(self, nums, start, end):
        if start == end:
            self.result.append(nums[:])
        for i in range(start, end):
            nums[i], nums[start] = nums[start], nums[i]
            self.dfs(nums, start + 1, end)
            nums[i], nums[start] = nums[start], nums[i]
        
# @lc code=end

