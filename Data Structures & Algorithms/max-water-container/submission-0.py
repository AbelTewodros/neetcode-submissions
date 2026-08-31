class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end=0,len(heights)-1
        maxi=0
        
        while start<end:
            current=min(heights[start],heights[end])*(end-start)
            if current>maxi:
                maxi=current
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        return maxi