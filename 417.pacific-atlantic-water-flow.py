#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:

    # 从两边大海往中间走，能走到哪里记录到哪里
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        # 1. eliminate empty case
        if not matrix: 
            return []

        # 2. variables Definition
        pacific_set = set()
        atlantic_set = set()
        n = len(matrix)
        m = len(matrix[0])

        def recurse(i, j, visited_set):
            # define base case
            if (i, j) in visited_set:
                return

            # 先加进去因为边界的全是可行的，而且下一步只有pass了matrix[new_i][new_j] >= matrix[i][j]
            # 条件的， 才会被放入recursion\
            visited_set.add((i, j))
            for dir_i, dir_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = dir_i + i, dir_j + j
                if 0 <= new_i < n and 0 <= new_j < m and \
                    matrix[new_i][new_j] >= matrix[i][j]:
                    recurse(new_i, new_j, visited_set)

        for row in range(n):
            recurse(row, 0, pacific_set)   
            recurse(row, m - 1, atlantic_set)   

        for col in range(m):
            recurse(0, col, pacific_set)   
            recurse(n - 1, col, atlantic_set)  

        return list(pacific_set & atlantic_set)    

# @lc code=end

