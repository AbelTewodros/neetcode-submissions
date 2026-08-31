import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end=max(piles)
        start=1
        k,hour_taken=float("inf"),0
        while start<=end:
            current=start+((end-start)//2)
            total=0
            for pile in piles:
                total+=(math.ceil(pile/current))
            if  total<=h:
                if current<k:
                    k,hour_taken=current,total
                end=current-1
            else:
                start=current+1
        return k
