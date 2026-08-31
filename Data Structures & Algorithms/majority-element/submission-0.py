from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxi = 0
        maxi_k = None
        for k in count.keys():
            if count[k] >= len(nums)/2:
                return k
            if count[k] > maxi:
                maxi = count[k]
                maxi_k = k
        return maxi_k