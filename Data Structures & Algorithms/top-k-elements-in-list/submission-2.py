from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        count = Counter(nums)
        bucket=[[] for i in range(len(nums))]
        for key,v in count.items():
            bucket[v-1].append(key)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for j in range(len(bucket[i])-1,-1,-1):
                if len(res) != k:
                    res.append(bucket[i][j])
                else:
                    break

        return res