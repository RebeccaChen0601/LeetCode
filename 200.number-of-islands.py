#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # forget to check null
        if not grid or not grid[0]:
            return 0

        visited = set()
        numOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(visited, grid, i, j)
                    numOfIslands += 1

        return numOfIslands

    def bfs(self, visited, grid, i, j):
        queue = collections.deque([(i, j)])
        visited.add((i, j))

        while queue:
            i, j = queue.popleft()
            for inc_i, inc_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i = i + inc_i
                new_j = j + inc_j
                if not self.isValid(grid, new_i, new_j, visited):
                    continue
                queue.append((new_i, new_j))
                visited.add((new_i, new_j))

    def isValid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        
        if (x, y) in visited:
            return False

        return grid[x][y] == '1'


        
# @lc code=end

