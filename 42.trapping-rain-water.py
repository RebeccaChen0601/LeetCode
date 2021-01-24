#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max, drops = 0, 0, 0
        while(left <= right):
            # 代表左边0到left的最大值
            l_max = max(l_max, height[left])
            # 代表右边right到末尾的最大值
            r_max = max(r_max, height[right])

            # 找l_max和r_max之间的较小值， 作为左右墙盛水的最低要求，用来求diff，并update
            if l_max < r_max:
                drops += (l_max - height[left])
                left += 1
            else:
                drops += (r_max - height[right])
                right -= 1
        return drops
# @lc code=end

