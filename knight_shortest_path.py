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

        queue = collections.deque(source)
        actions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        pathLen = 0
        visited = set()

        while queue:
            pathLen += 1
            for _ in range(len(queue)):
                position = queue.popleft()
                for inc_x, inc_y in actions:
                    new_x = position.x + inc_x
                    new_y = position.y + inc_y
                    if(new_x, new_y) == destination:
                        return pathLen
                    if self.isValid(new_x, new_y, position.x, position.y, visited, grid):
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
        
        return -1

    def isValid(self, x, y, old_x, old_y, visited, grid):
        if (x, y) in visited:
            return False
        if not (0 <= x < len(grid) and 0 <= y < len(grid)):
            return False
        barrier_x = 1 if x - old_x > 0 else -1
        barrier_y = 1 if y - old_y > 0 else -1
        if grid[old_x + barrier_x][y] and grid[old_x][old_y + barrier_y]:
            return False
        return grid[x][y]



