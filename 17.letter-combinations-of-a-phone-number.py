#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        res = []

        def dfs(word, digit_index):
            if len(word) == len(digits):   
                res.append(word)
                return  

            char_list = mapping[int(digits[digit_index])]
            for char in char_list:
                dfs(word + char, digit_index + 1)

        dfs("", 0)
        return res
        
# @lc code=end

