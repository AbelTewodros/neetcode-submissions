class Solution:
    def numDecodings(self, s: str) -> int:
        self.decoding_count = 0
        mem = {len(s):1}
        def helper(i):
            if i in mem:
                return mem[i]
            
            if s[i] == "0":
                return 0
            
            res = helper(i+1)

            if (i + 1) < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1]<="6")):
                res += helper(i+2)
            mem[i] = res
            return mem[i]
        
        return helper(0)
            
            
        


            




        
            

