class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        max_stack = []
        max_stack.append((temperatures[-1],len(temperatures)-1))

        for i in range(len(temperatures)-2,-1,-1):
            
            while max_stack and temperatures[i] >= max_stack[-1][0]:
                max_stack.pop()
            
            if max_stack:
                result[i] = max_stack[-1][1] - i
            max_stack.append((temperatures[i],i))
        
        return result