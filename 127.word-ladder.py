#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordset = set(wordList)
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        dist = 1

        while queue:
            dist += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + char + word[i+1:]  
                        if new_word in visited or new_word not in wordset:
                            continue
                        if new_word == endWord:
                            return dist
                        queue.append(new_word)
                        visited.add(new_word)

        return 0
        
# @lc code=end

