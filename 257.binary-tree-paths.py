#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        self.paths = []
        self.bfs(root, [])
        return self.paths
    
    def bfs(self, root, path):
        path.append(str(root.val))
        
        if root.left is None and root.right is None:
            self.paths.append('->'.join(path))
        if root.left:
            self.bfs(root.left, path)
            path.pop()
        if root.right:
            self.bfs(root.right, path)
            path.pop()

        
# @lc code=end

