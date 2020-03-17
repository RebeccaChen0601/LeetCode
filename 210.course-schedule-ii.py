#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return True
        
        mapping = {}
        in_degree = {}
        all_elem = set()
    
        for first, second in prerequisites:
            if first not in mapping:
                mapping[first] = set()
            if second not in in_degree:
                in_degree[second] = 0
            all_elem.add(first)
            all_elem.add(second)
            in_degree[second] += 1
            mapping[first].add(second)

        order = []
        
        start_node = [first for first in mapping.keys() if first not in in_degree]
        queue = collections.deque(start_node)

        while queue:
            node = queue.popleft()
            order.append(node)
            if node not in mapping:
                continue
            for neighbor in mapping[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        return True
# @lc code=end

