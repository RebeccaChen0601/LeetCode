#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(pivot, left, right):
            pivot_value = nums[pivot]
            nums[pivot], nums[right] = nums[right], nums[pivot]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def kSelect(left, right, k_small):
            if left == right: 
                return nums[left] # return the only element left in nums 
            pivot = random.randint(left, right)
            pivot = partition(pivot, left, right)
            if pivot == k_small:
                return nums[k_small]
            elif pivot < k_small:
                return kSelect(pivot + 1, right, k_small)
            else:
                return kSelect(left, pivot - 1, k_small)
        return kSelect(0, len(nums) - 1, len(nums) - k)
# @lc code=end

