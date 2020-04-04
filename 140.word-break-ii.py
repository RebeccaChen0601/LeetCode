#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:        
        return self.dfs(s, wordDict, "", {})
    
    def dfs(self, s, wordDict, sentence, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partition = []
        
        for i in range(len(s)):
            word = s[:i+1]
            if word not in wordDict:
                continue
            postfixes = self.dfs(s[i+1:], wordDict, sentence, memo)
            for postfix in postfixes:
                partition.append(word + " " + postfix)
                print(partition)

        if s in wordDict:
            partition.append(s)

        memo[s] = partition
        
        return memo[s]

# @lc code=end

