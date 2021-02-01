#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest, max_count = 0, 0, 0
        count = {}
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            max_count = max(max_count, count[s[right]])
            while right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
# @lc code=end

