class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while right>left and right>=0:
            middle=left+((right-left)//2)
            if nums[middle]<nums[right] and nums[middle]<nums[left]:
                left,right=left+1,right-1
            elif nums[middle]<nums[right]:
                right=middle-1
            else:
                left=middle+1
        return nums[left]




