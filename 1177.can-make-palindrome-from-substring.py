#
# @lc app=leetcode id=1177 lang=python3
#
# [1177] Can Make Palindrome from Substring
#

# @lc code=start
class Solution:
   def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [[0] * 26] # form a [[0, 0, ..., 0]] size = (1， 26) array
        for i, c in enumerate(s):
            # append a new len of 26 array with a basis copy from the privious one [[0, 0, ..., 0], [0, 0, ..., 0]] 
            cnt.append(cnt[i][:])
            # count the number appearance of each character
            cnt[i + 1][ord(c) - ord('a')] += 1
        # for all queries, return true for those requires less than k replacement
        # To determine how many replacement it needs, check how many odd count characters are
        # by suming the mod 2 results of all 26 characters' number of appearance in the (low, high) range
        # and divide that by 2 since we can let those character change into each other
        # then only half of them need to be modified. ex. 5 a's, 3 c's, only need to change all c to a
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]
        
# @lc code=end

