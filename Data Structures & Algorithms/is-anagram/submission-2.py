class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## If we sort then its nlogn
        ## If we add one to the dictionary thats n, then we check each in m-> n + m linear.
        if len(s) != len(t):
            return False
        deconstruction = dict()
        for i in s:
            deconstruction[i] = deconstruction.get(i,0) + 1
        for j in t:
            if j not in deconstruction.keys() or deconstruction[j] == 0:
                return False
            else:
                deconstruction[j] -= 1
        return True