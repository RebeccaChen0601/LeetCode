#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if len(prerequisites) == 0:
            return range(numCourses)

        mapping = {}
        in_degree = {}
        all_elem = set()
        
        for first, second in prerequisites:
            if second not in mapping:
                mapping[second] = set()
            if first not in in_degree: 
                in_degree[first] = 0
            mapping[second].add(first)
            in_degree[first] += 1
            all_elem.add(first)
            all_elem.add(second)

        start_node = [node for node in mapping.keys() if node not in in_degree]
        queue = collections.deque(start_node)
        order = []

        if numCourses > len(all_elem):
            for outlier in range(numCourses):
                 if outlier not in all_elem:
                    order.append(outlier)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            if node not in mapping:
                continue
            for neighbor in mapping[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if numCourses == len(order):
            return order
        return []

       
        # if len(prerequisites) == 0:
        #     return range(numCourses)
        
        # mapping = {}
        # in_degree = {}
        # all_elem = set()
    
        # for first, second in prerequisites:
        #     if second not in mapping:
        #         mapping[second] = set()
        #     if first not in in_degree:
        #         in_degree[first] = 0
        #     if first in mapping[second]:
        #         if second in mapping[first]:
        #             return []
        #         continue
        #     all_elem.add(first)
        #     all_elem.add(second)
        #     in_degree[first] += 1
        #     mapping[second].add(first)

        # order = []
        # if numCourses > len(all_elem):
        #     for outlier in range(numCourses):
        #          if outlier not in all_elem:
        #             order.append(outlier)
        
        # start_node = [second for second in mapping.keys() if second not in in_degree]
        # queue = collections.deque(start_node)

        # while queue:
        #     node = queue.popleft()
        #     order.append(node)
        #     if node not in mapping:
        #         continue
        #     for neighbor in mapping[node]:
        #         in_degree[neighbor] -= 1
        #         if in_degree[neighbor] == 0:
        #             queue.append(neighbor)
        
        # if len(order) == numCourses:
        #     return order
        # return []
# @lc code=end

