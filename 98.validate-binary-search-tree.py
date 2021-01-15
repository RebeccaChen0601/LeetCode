#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isValidHelper(node, left_bound, right_bound):
            if not node:
                return True

            # 如果左边 or 右边存在 children 但不满足 BST => False
            if (node.val >= right_bound or node.val <= left_bound):
                return False
            # 剩下的如果左边 or 右边只有存在 children就一定满足 BST 

            # 如果左边 or 右边不存在 children， 直接 True， 必须左右subtree都valid    
            return (isValidHelper(node.left, left_bound, node.val) 
                and isValidHelper(node.right, node.val, right_bound))

        return isValidHelper(root, float('-inf'), float('inf')) 
        
        
# @lc code=end

