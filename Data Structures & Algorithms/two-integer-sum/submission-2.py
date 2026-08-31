class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in prev.keys():
                return [prev[complement],i]
            prev[nums[i]] = i
