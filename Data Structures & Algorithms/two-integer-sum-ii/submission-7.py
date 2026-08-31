class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end=0,len(numbers)-1
        while start<end:
           t =target-(numbers[start]+numbers[end])
           if t==0:
            return [start+1,end+1]
           elif t>0:
            start+=1
           else:
            end-=1
            