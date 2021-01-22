#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 必须sort 因为dp需要从先把最短word的insertion次数fill好，然后逐渐增加长度
        words.sort(key=len)

        # dp代表目前到这个形态经历了多少次insertion
        dp = {word: 1 for word in words}
        longest = 1

        for word in words:
            # iterate on 所有的选择
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    # 状态转移function
                    dp[word] = dp[predecessor] + 1
                    longest = max(longest, dp[word])
        return longest

        
# @lc code=end

