class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_sum = sum(nums)
        
        summed_true = (len(nums))*(len(nums)+1)
        summed_true //=2
        return summed_true - list_sum

