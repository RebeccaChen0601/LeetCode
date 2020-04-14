#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        queue = collections.deque([root])
        
        index = 0

        while index < len(queue):    
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        while queue[-1] is None:
            queue.pop()
        return '[%s]'%','.join( [str(node.val) if node is not None else 'null' for node in queue])

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')
        if data == '[]':
            return None
        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        isLeft = True
        index = 0

        for val in vals[1:]:
            if val != 'null':
                node = TreeNode(int(val))
                if isLeft:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not isLeft:
                index += 1
            isLeft = not isLeft

        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

