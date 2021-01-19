#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            # stack = [-1]
            # maxArea = 0

            # for i in range(len(heights)):
            #     while heights[i] <= heights[stack[-1]] and stack[-1] != -1:
            #         maxArea = max(maxArea, (i - stack[-1] - 1) *  heights[stack.pop()])
            #     stack.append(i)
            # while stack[-1] != -1: 
            #     maxArea = max(maxArea, (len(heights)  - stack[-1] - 1) *  heights[stack.pop()])
                
            # return maxArea
            stack = [-1]
            maxarea = 0
            for i in range(len(heights)):

                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)

            while stack[-1] != -1:
                maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
            return maxarea

        if not matrix: return 0
        finalMaxArea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0 
            finalMaxArea = max(finalMaxArea, largestRectangleArea(dp))

        return finalMaxArea


# @lc code=end

