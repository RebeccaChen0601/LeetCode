#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(target, start, num_list):
            if target == 0:
                res.append(list(num_list))
                return 
            if target < 0: 
                return
            for i in range(start, len(candidates)):
                num_list.append(candidates[i])
                dfs(target - candidates[i], i, num_list)
                num_list.pop()
        dfs(target, 0, [])
        return res
        
# @lc code=end

