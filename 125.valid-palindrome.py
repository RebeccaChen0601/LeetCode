#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while True:
            while left < len(s) and not self.isNumericAlpha(s[left]):
                left += 1
            while right > 0 and not self.isNumericAlpha(s[right]):
                right -= 1
            if left >= right:
                return True
            elif s[left].lower() != s[right].lower():
                return False
            else:
                (left, right) = (left + 1, right - 1)

    def isNumericAlpha(self, char):

        return (('a' <= char <= 'z') or 
            ('A' <= char <= 'Z') or 
            ('0' <= char <= '9'))
        
        
# @lc code=end

