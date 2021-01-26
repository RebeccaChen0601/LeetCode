#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i] == ')' and len(stack) == 0:
                s = s[:i] + s[i+1:]
                i -= 1
            elif s[i] == ')':
                stack.pop()
            elif s[i] == '(':
                stack.append(i)
            i += 1
        
        while len(stack) != 0:
            i = stack.pop()
            s = s[:i] + s[i+1:]

        return s
# @lc code=end

