class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s=set(nums)
        longest=0
        for i in nums_s:
            if i-1 not in nums_s:
                length=1
                while i+length in nums_s:
                    length+=1
                longest=max(length,longest)
        return longest





        

