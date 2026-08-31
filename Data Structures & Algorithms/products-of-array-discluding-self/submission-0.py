class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prefix(nums):
            pref=[1]*len(nums)
            for i in range(1,len(nums)):
                pref[i]=pref[i-1]*nums[i-1]
            return pref
        def suffix(nums):
            suff=[1]*len(nums)
            for i in range(len(nums)-2,-1,-1):
                suff[i]=suff[i+1]*nums[i+1]
            return suff
        pre=prefix(nums)
        suff=suffix(nums)
        for i in range(len(pre)):
            pre[i]=pre[i]*suff[i]
        return pre