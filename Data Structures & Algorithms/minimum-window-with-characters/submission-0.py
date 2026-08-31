class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        countT,window={},{}
       
        for c in t:
            countT[c]=1+countT.get(c,0)
        
        have,need=0,len(countT)
        res, resLen=[-1,-1],float('inf')
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            
            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1 
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLen!=float('inf') else ""
                 
       
       
       
       
       
       
        # for i in range(len(t)):
        #     if s[i] in have:
        #         have[s[i]]+=1
        #     need[t[i]]+=1
        # matches=0
        # for k,v in have.items():
        #     if have[k]>=need[k]:
        #         matches+=1
        
        # left=0
        # mini=float('inf')
        # res=None
        # for right in range(len(t),len(s)):
        #     if matches==len(need):
        #         if right-left+1<mini:
        #             mini=right-left+1
        #             res=left,right
        #         while matches==len(need):
        #             if s[left] in have:
        #                 have[s[left]]-=1
        #                 matches-=1 if have[s[left]]<need[s[left]] else 0
        #             left+=1
        #     if s[right] in have:
        #         have[s[right]]+=1
        #         matches+=1 if have[s[right]]==need[s[right]] else 0
        #     if s[left] not in have:
        #         left+=1
        
        # return s[res[0]:res[1]]
    
    
    
    
    
    
    
    
    
    
    #     if len(s)<len(t):
    #         return ""
    # sCount,tCount,t_check=[0]*52,[0]*52,[]
    # for i in range(len(t)):
    #     sCount[self.get_ind(s[i])]+=1
    #     tCount[self.get_ind(t[i])]+=1
    #     t_check.append(self.get_ind(t[i]))
    # matches=0
    # for i in t_check:
    #     if sCount[i]==tCount[i]:
    #         matches+=1 
    
    # mini=float('inf')
    # left=0
    # for right in range(len(t),len(s)):
    #     if right-left+1 == len(t) and matches==len(t):
    #         return s[left:right]
    #     elif right-left+1 >len(t) and matches==len(t):
    #         mini=min(mini,right-left+1)
    #         left+=1
    #         sCount[left]-=1
    #         matches-=1 if left in t_check else 0
    #         continue
        
    #     index=get_ind(s[left])
    #     if index not in t_check:
    #         left+=1
        

    
    # def get_ind(self,a):
    #     if 123>=ord(a)>=97:
    #         return ord(a)-ord('a')
    #     else:
    #         return ord(a)-ord('A')

