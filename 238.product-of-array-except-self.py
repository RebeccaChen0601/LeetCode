#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        n = len(nums)
        for num in nums[1:]:
            output.append(output[-1]*num)
        output[-1] = 1
        for i in range(n-1, 0, -1):
            output[i - 1] = output[i] * output[i - 1]
            output[i] = output[i] * nums[i]
            output[i], output[i - 1] = output[i - 1], output[i] 
        return output   

# @lc code=end

