#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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
        
        if(len(all_elem) != len(order)):
            return False
        
        return True
# @lc code=end

