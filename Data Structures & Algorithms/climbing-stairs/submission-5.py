class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {0:1,1:1}
        def fib(l):
            if l in dic.keys():
                return dic[l]
            dic[l] =fib(l-1) + fib(l-2)
            return dic[l]
               
        fib(n)
        return dic[n]
    