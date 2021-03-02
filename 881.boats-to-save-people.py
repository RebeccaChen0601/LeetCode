#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, ans = 0, len(people) - 1, 0
        while left <= right:
            light, heavy = people[left], people[right]
            if light + heavy <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                ans += 1
                right -= 1
        return ans


        
# @lc code=end

