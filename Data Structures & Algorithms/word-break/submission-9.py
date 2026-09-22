class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def helper(idx):
            if idx >= len(s):
                return True
            if idx in memo:
                return memo[idx]

            for word in wordDict:
                if s[idx] == word[0] and idx+len(word) <= len(s) and s[idx:idx+len(word)] == word:

                    if helper(idx+len(word)) == True:
                        memo[idx] = True
                        return memo[idx]

            memo[idx] = False
            return memo[idx]


        return helper(0)