class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## If we sort then its nlogn
        ## If we add one to the dictionary thats n, then we check each in m-> n + m linear.
        return sorted(s) == sorted(t)