#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import random
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def findDist(i):
            return points[i][0] ** 2 + points[i][1] ** 2
        def partition(low, high):
            pivot = low
            low += 1
            while True:
                while low < high and findDist(low) < findDist(pivot):
                    low += 1
                while low <= high and findDist(high) >= findDist(pivot):
                    high -= 1
                if low >= high: break
                points[low], points[high] = points[high], points[low]
            points[pivot], points[high] = points[high], points[pivot]
            return high
        def sort(low, high, K):
            if low >= high: return
            k = random.randint(low, high)
            points[low], points[k] = points[k], points[low]
            pivot = partition(low, high)
            if K < (pivot - low + 1):
                sort(low, pivot - 1, K)
            elif K > pivot - low + 1:
                sort(pivot + 1, high, K - pivot + 1)
        sort(0, len(points) - 1, K)
        return points[:K]
# @lc code=end

