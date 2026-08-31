class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        mini=float("inf")
        while right>=left:
            if nums[left]<nums[right]:
                mini=min(nums[left],mini)
                break

            middle=left+((right-left)//2)
            mini=min(nums[middle],mini)
            
            if nums[middle]>=nums[left]:
                left=middle+1
            else:
                right=middle-1
        return mini







