"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here

        visited = set() 

        if not (self.isValid(source.x, source.y, visited, grid) or 
        self.isValid(destination.x, destination.y, visited, grid)):
            return -1

        queue = collections.deque([(source.x, source.y)])
        visited.add((source.x, source.y))
        pathLen = 0
        

        while queue:
            pathLen += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for inc_x, inc_y in [(1, 2), (1, -2), (-1, 2), 
                (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    new_x = x + inc_x
                    new_y = y + inc_y
                    if self.isValid(new_x, new_y, visited, grid):
                        if new_x == destination.x and new_y == destination.y:
                            return pathLen
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
        
        return -1

    def isValid(self, x, y, visited, grid):
        if (x, y) in visited:
            return False
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        ####?????/ why don't check 蹩脚马？？？？？？？？？？？？？？？？？
        # barrier_x = 1 if x - old_x > 0 else -1
        # barrier_y = 1 if y - old_y > 0 else -1
        # check_x = old_x + barrier_x
        # check_y = old_y + barrier_y
        # if (0 <= check_x < len(grid) and 0 <= check_y <= len(grid[0])):
        #     if grid[old_x + barrier_x][y] and grid[old_x][old_y + barrier_y]:
        #         return False
        return not grid[x][y]