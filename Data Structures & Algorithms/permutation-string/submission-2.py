from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = [0]*26
        for i in s1:
            s1_counter[ord(i)-ord('a')] += 1
        s2_counter = [0]*26

        left,right = 0,0
        while right < len(s1):
            s2_counter[ord(s2[right])-ord('a')] += 1
            right += 1
        while right < len(s2):
            if s1_counter == s2_counter:
                return True
            else:
                s2_counter[ord(s2[left])-ord('a')] -= 1
                left+=1
                s2_counter[ord(s2[right])-ord('a')] += 1
                right+=1
                
        return  s2_counter == s1_counter 

        