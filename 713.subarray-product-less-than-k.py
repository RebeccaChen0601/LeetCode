#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count = 0
        product = 1
        while right < len(nums):  
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1      
            right += 1   
            count += (right - left)
        return count
        
        
# @lc code=end

