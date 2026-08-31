class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [1]* len(nums)
        for i in range(len(nums)-2,-1,-1):
            right_product[i] = right_product[i+1] * nums[i+1]
        
        left_product = 1
        for j in range(len(nums)):
            right_product[j] = right_product[j] * left_product
            left_product *= nums[j]
        return right_product
