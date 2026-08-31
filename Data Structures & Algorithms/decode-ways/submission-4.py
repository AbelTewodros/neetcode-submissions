class Solution:
    def numDecodings(self, s: str) -> int:
        dic={str(key-64):chr(key) for key in range(65,91) }
        count=0
       
        def dfs(i):
            nonlocal count
            if i==len(s) :
                return 1
            if s[i]=='0':
                return 0
            ways=dfs(i+1)
            if i+1< len(s) and (s[i]=='1' or (s[i]=='2' and s[i+1]<='6')):
                ways+=dfs(i+2)
            return ways
                
        return dfs(0)
   

