class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, len(height)-1
        left, right = 0, len(height)-1
        area = 0

        while left <= right:
            if height[left_max] <= height[right_max]:
                left_max = left_max if height[left_max]>height[left] else left
                area += height[left_max] - height[left]
                left += 1
            else:
                right_max = right_max if height[right_max] > height[right] else right
                area += height[right_max] - height[right]
                right -= 1
        return area 