class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def helper(start,end):
            rob1,rob2 = 0,0
            for n in range(start,end):
                temp = max(rob1+nums[n],rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0],helper(0,len(nums)-1),helper(1,len(nums)))
            