#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        left, right, mid = 0, len(A) - 1, 0
    
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target > A[mid]:
                left = mid
            else:
                right = mid

        list = []
        next = 0
        for i in range(0, k):
            if left >= 0 and right < len(A):
                left_diff = abs(A[left] - target) 
                right_diff = abs(A[right] - target)
                
                if (left_diff < right_diff) or (A[left] <= A[right] and left_diff == right_diff):
                    next = A[left]
                    left -= 1
                elif (left_diff > right_diff) or (A[left] > A[right] and left_diff == right_diff):
                    next = A[right]
                    right += 1
                print(next)
            elif left >= 0:
                next = A[left]
                left -= 1
            elif right < len(A):
                next = A[right]
                right += 1
                print(next)
            list.append(next)

        return list

            



        
# @lc code=end

