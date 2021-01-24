#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {char:index for index, char in enumerate(order)}
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            
            for j in range(min(len(word_1), len(word_2))): 
                if word_1[j] != word_2[j]:
                    if dictionary[word_1[j]] > dictionary[word_2[j]]:
                        return False 
                    break
            else:
                if len(word_1) > len(word_2):
                    return False
        return True
# @lc code=end

