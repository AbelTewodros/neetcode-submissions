class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cal={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in cal.keys():
                return sorted([i,cal[diff]])
            cal[nums[i]]=i
        return -1