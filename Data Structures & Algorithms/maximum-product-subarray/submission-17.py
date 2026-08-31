class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest=1
        smallest=1
        glob_max=nums[0]

        for num in nums:
            temp=biggest*num
            biggest=max(biggest*num,smallest*num,num)
            smallest=min(temp,smallest*num,num)
            glob_max=max(biggest,glob_max)
        return glob_max
