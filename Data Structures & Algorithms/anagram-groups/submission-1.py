class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = {}
        for i in strs:
            fixed = str(sorted(i))
            
            if fixed in main.keys():
                main[fixed].append(i)
            else:
                main[fixed] = [i]
        return [i for i in main.values()]