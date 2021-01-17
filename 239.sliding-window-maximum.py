#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        output = []
        l = r = 0

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.popleft()
            if r + 1 - l >= k:
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output
# @lc code=end

