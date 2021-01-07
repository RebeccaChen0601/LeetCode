#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        queue = collections.deque([node])
        visited = set([node])

        @functools.cache
        def get_node(node):
            return Node(node.val)

        while queue:
            n = queue.popleft()
            nnode = get_node(n)
            neighbors = []
            for neighbor in n.neighbors:
                neighbors.append(get_node(neighbor))
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            nnode.neighbors = neighbors

        return get_node(node)



        
# @lc code=end

