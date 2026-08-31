class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)-1

        while start<=end:
            m=start+((end-start)//2)
            if nums[m]==target:
                return m
            elif nums[m]>target:
                end=m-1
            else:
                start=m+1
        return -1
