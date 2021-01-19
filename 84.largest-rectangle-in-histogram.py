#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        maxArea = float('-inf')

        for i in range(len(heights)):
            while heights[i] <= heights[stack[-1]] and stack[-1] != -1:
                height = heights[stack.pop()]
                maxArea = max(maxArea, (i - stack[-1] - 1) * height)
            stack.append(i)
        while stack[-1] != -1: 
            print(stack)
            height = heights[stack.pop()]
            maxArea = max(maxArea, (len(heights)  - stack[-1] - 1) * height)
            print(maxArea)
            
        return maxArea

        # stack = [-1]
        # maxArea = 0

        # for i in range(len(heights)):
        #     while heights[i] <= heights[stack[-1]] and stack[-1] != -1:
        #         maxArea = max(maxArea, (i - stack[-1] - 1) *  heights[stack.pop()])
        #     stack.append(i)
        # while stack[-1] != -1: 
        #     maxArea = max(maxArea, (len(heights)  - stack[-1] - 1) *  heights[stack.pop()])
            
        # return maxArea
# @lc code=end

