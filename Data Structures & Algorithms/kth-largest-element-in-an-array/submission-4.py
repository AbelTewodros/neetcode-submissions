class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        def quickselect(start,end):
            p,pivot= start,nums[end]
            for i in range(start,end):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[end]=nums[end],nums[p]
            if p>k:
                return quickselect(start,p-1)
            elif p<k:
                return quickselect(p+1,end)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)
