from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        hash_t = Counter(t)
        total_sum = sum(x for x in hash_t.values())
        ans_len = float("inf")
        idx_1,idx_2 = -1,-1
        

        i = 0
        while i < len(s) and s[i] not in hash_t:
                i += 1
        if i >= len(s):
            return ""
        
        j = i

        while j < len(s):
            if s[j] in hash_t:
                if hash_t[s[j]] > 0:
                    total_sum -= 1
                hash_t[s[j]] -= 1
            while total_sum == 0:
                if (j-i+1) < ans_len:
                    idx_1 = i
                    idx_2 = j
                    ans_len = j-i + 1
                if s[i] in hash_t:
                    hash_t[s[i]] += 1
                    if hash_t[s[i]] > 0:
                        total_sum += 1
                i += 1
            j += 1

        return "" if idx_1 == -1 else s[idx_1:idx_2+1]


