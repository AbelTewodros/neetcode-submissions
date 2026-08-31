import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=sorted(list(zip(position,speed)))
        stack=[]
        for i in range(len(pair)-1,-1,-1):
            stack.append((target-pair[i][0])/pair[i][1])
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

            
                

