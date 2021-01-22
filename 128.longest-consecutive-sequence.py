#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        visited = set()
        numSet = set(nums)

        for num in nums:
            if num in visited:
                continue
            total = 1
            accessor = num + 1
            decessor = num - 1
            while accessor in numSet:
                visited.add(accessor)
                total +=  1
                accessor += 1
                
            while decessor in numSet:
                visited.add(decessor)
                total +=  1
                decessor -= 1
            longest = max(total, longest)    
            visited.add(num)

        return longest

# @lc code=end

