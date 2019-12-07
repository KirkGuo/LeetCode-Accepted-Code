class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [-1]
        for idx, each in enumerate(heights):
            while stack[-1]!=-1 and heights[stack[-1]] > each:
                height = heights[stack.pop(-1)]
                tmp_sqr = height * (idx - stack[-1] - 1)
                ans = max(ans, tmp_sqr)
            stack.append(idx)
        
        tmp = 0
        while stack[-1]!=-1:
            height = heights[stack.pop(-1)]
            tmp_sqr = height * (idx - stack[-1])
            ans = max(ans, tmp_sqr)
        
        return max(ans, tmp*len(heights))
