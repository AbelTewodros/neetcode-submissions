class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem = {}
        
        def helper(idx):
            if idx >= len(nums):
                return 0
            if idx in mem:
                return mem[idx]

            mem[idx] = max(nums[idx]+helper(idx+2),helper(idx+1))
            return mem[idx]
        return helper(0)