class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = float("-inf")
        currMax, currMin = 1,1
        
        for num in nums:
            curr = currMax * num
            currMax = max(num, curr, currMin*num)
            currMin = min(currMin*num,num, curr)
            res = max(res,currMax)
        return res




            