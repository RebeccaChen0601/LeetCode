#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return True

        memo[s] = False
        
        for i in range(len(s)):
            word = s[:i+1]
            if word not in wordDict:
                continue
            if self.dfs(s[i+1:], wordDict, memo):
                memo[s] = True
                break
        
        return memo[s]


        
# @lc code=end

