class Solution:
    def countSubstrings(self, s: str) -> int:
        count_palindrome = 0

        for n in range(len(s)):
            i = j = n
            while i >= 0 and j < len(s):
                if  s[i] == s[j]:
                    count_palindrome += 1
                elif s[i] != s[j]:
                    break
                i -= 1
                j += 1
        for n in range(len(s)):
            i,j = n-1, n
            while i >=0 and j < len(s):
                if s[i] == s[j]:
                    count_palindrome += 1
                elif s[i] != s[j]:
                    break
                i -= 1
                j += 1
        return count_palindrome