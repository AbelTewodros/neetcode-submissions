class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_most = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)
        right_most = [len(heights)] * len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(len(left_most)):
            left_most[i] += 1
            right_most[i] -= 1
            max_area = max(max_area, (heights[i] * (right_most[i] - left_most[i] + 1)))
        return max_area