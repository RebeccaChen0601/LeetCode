#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        def dfs(node, current_sum):
            if node is None:
                return
            current_sum += node.val
            if current_sum == sum:
                self.count += 1
            self.count += mapping[current_sum - sum]
            mapping[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            mapping[current_sum] -= 1
        mapping = defaultdict(int)
        dfs(root, 0)
        
        return self.count

# @lc code=end

