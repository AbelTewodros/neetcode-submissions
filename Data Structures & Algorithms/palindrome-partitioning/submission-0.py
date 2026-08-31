class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        subset=[]
        def dfs(i,j):
            if i>=len(s):
                if i==j:
                    res.append(subset.copy())
                return
            if is_palindrome(s[j:i+1]):
                subset.append(s[j:i+1])
                dfs(i+1,i+1)
                subset.pop()
            dfs(i+1,j)
        def is_palindrome(s):
            i,j=0,len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        dfs(0,0)
        return res




            