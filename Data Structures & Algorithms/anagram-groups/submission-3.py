from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for text in strs:
            new_txt = ''.join(sorted(text))
            groups[new_txt].append(text)
        res = []
        for k in groups.keys():
            res.append(groups[k])
        return res