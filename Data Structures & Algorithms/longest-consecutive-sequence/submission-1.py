class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dict={val:ind for ind,val in enumerate(nums)}
        seq_max=[]
        counter=[]
        for i in nums:
            if i-1 not in dict:
                seq_max.append(i)
      
        for i in seq_max:
            s=i+1
            c=1
            while s in dict:
                c+=1
                s+=1
            counter.append(c)
        return max(counter)


        

