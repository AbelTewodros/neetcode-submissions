from collections import Counter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list =[(p,s) for p,s in zip(position,speed)]
        sorted_list.sort(reverse= True)
        stack = []

        for p,s in sorted_list:
            steps = ((target - p)/s)
            if stack and steps <= stack[-1]:
                continue
            stack.append(steps)
        return len(stack)
            


            