class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mem={}
        for index,number in enumerate(numbers):
            complement=target-number
            if complement in mem:
                return [mem[complement],index+1]
            mem[number]=index+1