class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left<=right:
            middle=left+(right-left)//2

            if nums[middle]==target:
                return middle
            
            if nums[middle]>=nums[left]:
                if nums[left]>target or target>nums[middle]:
                    left=middle+1
                else:
                    right=middle-1
                    
            
            else:
                if target>nums[right] or target<nums[middle]:
                    right=middle-1
                else:
                    left=middle+1
        return -1


                
