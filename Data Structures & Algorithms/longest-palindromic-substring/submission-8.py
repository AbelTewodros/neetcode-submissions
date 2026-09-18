class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_i,max_j = 0,0

        for n in range(len(s)):
            i,j = n,n
            while i >= 0 and j < len(s):
                if s[i]!= s[j]:
                    break
                if (j-i) > max_j-max_i:
                    max_i,max_j = i,j
                i -= 1
                j += 1
        
        for n in range(len(s)):
            i,j = n,n+1
            while i >= 0 and j < len(s):
                if s[i]!=s[j]:
                    break
                if (j-i) > max_j-max_i:
                    max_i, max_j = i,j
                i-=1
                j+=1
        return s[max_i:max_j+1]

                
