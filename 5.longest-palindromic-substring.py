#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        longleft, longright, longest = 0, 0, 0
        for i in range(len(s)):
            left1, right1, length1 = self.centerPalindrome(s, i, i + 1)
            left2, right2, length2 = self.centerPalindrome(s, i - 1, i + 1)
            left, right, length = (left1, right1, length1) if length1 > length2 else (left2, right2, length2)
            print(left, right, length)
            if length > longest:
                longest = length
                longleft, longright = left, right
        return s[longleft:longright + 1]
    
    def centerPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return left + 1, right - 1, right - left - 1 
        
# @lc code=end

