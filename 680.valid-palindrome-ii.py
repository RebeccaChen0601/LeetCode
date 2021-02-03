#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.deleted = False

        def isValid(left, right):
            if left >= right:
                return True
            if s[left] == s[right]:
                return isValid(left + 1, right - 1)
            elif not self.deleted:
                self.deleted = True
                return isValid(left + 1, right) or isValid(left, right - 1)
            return False
        return isValid(0, len(s) - 1)
# @lc code=end

