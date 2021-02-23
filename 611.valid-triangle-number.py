#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # 正思路
        if not nums:
            return 0
        nums.sort()
        count = 0
        for k in range(len(nums)):
            left, right = 0, k - 1
            while left < right:
                if nums[right] + nums[left] > nums[k]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count

        # 反思路
        # if not nums:
        #     return 0
        # nums.sort()
        # ans = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     left = 0
        #     right = i - 1
        #     while left < right:
        #         if nums[left] + nums[right] > nums[i]:
        #             ans += (right - left)
        #             right -= 1
        #         else:
        #             left += 1
        # return ans

        
# @lc code=end

