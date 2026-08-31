class Solution:
    def numDecodings(self, s: str) -> int:
        count=0
        dp={len(s):1}

        def dfs(i):

            if i in dp:
                return dp[i]
            if s[i]=='0':
                return 0
            res=dfs(i+1)
            if i+1<len(s) and ((s[i]<"2") or (s[i]=="2" and s[i+1]<="6")):
                res+=dfs(i+2)
            dp[i]=res
            return res
        
        return dfs(0)
        
            

# When can we stop well when we have a leading 0 or a 0 on its own we stop
# If the leading number is bigger than 1 so 2 and the second number is bigger
# than 26 we stop. These are the two cases we have to worry about.
            