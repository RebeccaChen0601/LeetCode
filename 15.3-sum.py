#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i + 1, len(nums) - 1, -nums[i])
        return self.result

    def twoSum(self, nums, left, right, target):
        while left < right:
            ans = nums[left] + nums[right]
            if ans == target:
                self.result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif ans > target:
                right -= 1
            else:
                left += 1
        
# @lc code=end

