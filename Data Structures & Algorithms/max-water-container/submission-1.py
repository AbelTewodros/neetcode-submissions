class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        curr = None
        left, right = 0, len(heights)-1
        while left < right:
            curr = min(heights[left],heights[right])* (right-left)
            maxi = max(maxi,curr)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
        return maxi