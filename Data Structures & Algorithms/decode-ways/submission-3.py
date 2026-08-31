class Solution:
    def numDecodings(self, s: str) -> int:
        dic={str(key-64):chr(key) for key in range(65,91) }
        count=0
       
        def dfs(i,j):
            nonlocal count
            if j>=len(s) :
                count+=1 if i==j else 0
                return
            if int(s[i:j+1])>26 or int(s[i:j+1])<1:
                return
            if s[i:j+1] in dic:
                dfs(j+1,j+1)
            dfs(i,j+1)
        dfs(0,0)
        return count

