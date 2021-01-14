#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if len(input) == 0:
            return []
        
        @functools.cache
        def dfs(input):
            if input.isnumeric():
                return [int(input)]
            
            res = []
            for i in range(len(input)):
                if input[i] in "+-*":
                    values1 = dfs(input[:i])
                    values2 = dfs(input[i+1:])
                    if input[i] == "+":
                        res += [v1 + v2 for v1 in values1 for v2 in values2]
                    elif input[i] == "-":
                        res += [v1 - v2 for v1 in values1 for v2 in values2]
                    else:
                        res += [v1 * v2 for v1 in values1 for v2 in values2]
            return res
        return dfs(input)
# @lc code=end

