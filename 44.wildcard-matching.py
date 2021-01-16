#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.cache
        def dfs(s_i, p_i):
            if len(s) == s_i and len(p) == p_i:
                return True
            if len(s) > s_i and len(p) == p_i:
                return False
            if len(s) == s_i and len(p) > p_i:
                return p[p_i] == '*' and dfs(s_i, p_i + 1)
                
            pattern = p[p_i]
            source = s[s_i]

            if pattern == "?" or source == pattern:
                return dfs(s_i + 1, p_i + 1)
            if pattern == "*":
                return dfs(s_i + 1, p_i) or dfs(s_i, p_i + 1)
            
            return False
        return dfs(0, 0)
            
    
        
# @lc code=end

