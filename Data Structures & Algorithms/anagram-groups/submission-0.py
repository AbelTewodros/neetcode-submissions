class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new=defaultdict(list)
        for s in strs:
            count=[0]*26
            for l in s:
                count[ord(l)-ord('a')]+=1
            new[tuple(count)].append(s)
        return new.values()
        
