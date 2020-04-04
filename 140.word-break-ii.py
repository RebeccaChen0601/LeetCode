#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:   
       # write your code here        
        if not wordDict:
            return []
        maxLen = max([len(word) for word in wordDict])    
        return self.dfs(s, wordDict, "", maxLen, {})
    
    def dfs(self, s, wordDict, sentence, maxLen, memo):

        if len(s) == 0:
            return []
        
        if s in memo:
            return memo[s]

        partition = []
        end = min(maxLen, len(s))
        
        for i in range(end):
            word = s[:i+1]
            if word not in wordDict:
                continue
            postfixes = self.dfs(s[i+1:], wordDict, sentence, maxLen, memo)
            for postfix in postfixes:
                partition.append((word + " " + postfix).rstrip())
        if s in wordDict:
            partition.append(s)

        memo[s] = partition

        return partition

# @lc code=end

