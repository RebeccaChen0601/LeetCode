#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        result = []

        while queue:
            
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + char + word[i+1:]  
                        if new_word in visited or new_word not in wordset:
                            continue
                        if new_word == endWord:
                            return result
                        queue.append(new_word)
                        visited.add(new_word)

        return []
# @lc code=end

