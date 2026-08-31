class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = defaultdict(list)
        for i in strs:
            freq = [0]*26
            for l in i:
                freq[ord(l)-ord('a')] += 1
            main[tuple(freq)].append(i)
        return list(main.values())