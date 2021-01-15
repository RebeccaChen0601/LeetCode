#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(inorder) == 0:
            return None

        root_val = preorder.pop(0)
        node = TreeNode(val=root_val)

        index_root = inorder.index(root_val)

        node.left = self.buildTree(preorder, inorder[:index_root])
        node.right = self.buildTree(preorder, inorder[index_root+1:]) 
        
        return node
# @lc code=end

