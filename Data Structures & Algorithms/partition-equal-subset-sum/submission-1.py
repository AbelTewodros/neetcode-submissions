class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False

        total/=2
        curr=0
        subset1=set() ###a set of indexes so that retrieving is O(1)
        
        def partition(i):
            nonlocal curr,total,subset1
            if curr==total:
                return
            if i>=len(nums):
                return
            if nums[i]+curr>total:
                partition(i+1)
            else:
                subset1.add(i)
                curr+=nums[i]
                partition(i+1)
            if curr!=total and i in subset1:
                curr-=nums[i]
                subset1.remove(i)
                partition(i+1)
                     
                
        partition(0)
        return sum(nums[i] for i in subset1)==total