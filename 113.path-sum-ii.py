#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, targetSum, path):
            if not root:
                return 
            if root.left is None and root.right is None:
                if targetSum - root.val == 0:
                    path.append(root.val)
                    result.append(list(path))
                    path.pop()
                    return 
                return
            path.append(root.val)
            dfs(root.left, targetSum - root.val, path)
            dfs(root.right, targetSum - root.val, path)
            path.pop()
        dfs(root, targetSum, [])
        return result
# @lc code=end

