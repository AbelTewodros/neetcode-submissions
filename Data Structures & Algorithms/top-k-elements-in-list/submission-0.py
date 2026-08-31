class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        fre=[[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]=1+count.get(num,0)
        for key,value in count.items():
            fre[value].append(key)
        
        res=[]
        for i in range(len(fre) - 1,0, -1):
            for num in fre[i]:
                res.append(num)
                if len(res)==k:
                    return res
