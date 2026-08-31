class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfied = 0
        idx_g = 0
        idx_s = 0

        while idx_g < len(g) and idx_s < len(s):
            if s[idx_s] >= g[idx_g]:
                satisfied += 1
                idx_g += 1
                idx_s += 1
            else:
                idx_s += 1
        return satisfied