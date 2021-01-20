#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def turnWheel(node, i):
            if node[i] in "12345678":
                up = str(int(node[i]) + 1)
                down = str(int(node[i]) - 1)
            elif node[i] == "0":
                up = "1"
                down = "9"
            else:
                up = "0"
                down = "8"
            return [node[:i] + up + node[i+1:],\
                    node[:i] + down + node[i+1:]]

        if target == "0000":
            return 0
        queue = collections.deque(['0000'])
        if queue[0] in deadends:
            return -1
        visited = set()
        steps = 0

        while queue:
            steps += 1 
            for _ in range(len(queue)):
                node = queue.popleft()
                for i in range(len(node)):
                    for new_node in turnWheel(node, i):
                        if new_node in deadends:
                            continue
                        if new_node == target:
                            return steps
                        if new_node not in visited:
                            visited.add(new_node)
                            queue.append(new_node)
        return -1
# @lc code=end

