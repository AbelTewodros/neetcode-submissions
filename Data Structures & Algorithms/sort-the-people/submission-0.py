class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        idx = list(range(len(names)))
        idx.sort(key= lambda x: -heights[x] )
        return [names[i] for i in idx]