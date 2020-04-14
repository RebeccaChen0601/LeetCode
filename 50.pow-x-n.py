#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = self.myPow(x, abs(n) // 2)
        res *= res
        if n % 2 == 1:
            res *= x 
        res = 1/res if n < 0 else res
        return res
            
        
# @lc code=end

