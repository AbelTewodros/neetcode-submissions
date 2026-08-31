class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chekr = set()
        for i in nums:
            if i in chekr:
                return True
            chekr.add(i)
        return False