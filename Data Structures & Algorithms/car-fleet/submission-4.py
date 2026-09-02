from collections import Counter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = sorted(zip(position,speed))
        position,speed = zip(*sorted_list)
        total_steps = [(target - position[i])/speed[i] for i in range(len(position))]
        prev = total_steps[-1]
        fleet = 1

        for i in range(len(total_steps)-2,-1,-1):
            if total_steps[i] > prev:
                fleet += 1
                prev = total_steps[i]
        return fleet


            