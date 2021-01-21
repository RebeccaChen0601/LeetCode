#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(lambda: 0)
        prefix[0] = 1
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            prefix[count] += 1
            if count >= k:
                ans += prefix[count - k]
        return ans
# @lc code=end

