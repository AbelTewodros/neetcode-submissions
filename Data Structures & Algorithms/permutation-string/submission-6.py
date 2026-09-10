class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = [0]*26
        for i in s1:
            s1_counter[ord(i)-ord('a')] += 1
        
        s2_counter = [0]*26
        for j in range(len(s1)):
            s2_counter[ord(s2[j])-ord('a')] += 1
        
        matches = 0
        for k in range(len(s1_counter)):
            if s1_counter[k] == s2_counter[k]:
                matches += 1
        
        left = 0
        for right in range(len(s1),len(s2)):
            if matches == 26:
                return True
            right_idx = ord(s2[right])-ord('a')
            s2_counter[right_idx] += 1
            if s2_counter[right_idx] - 1 == s1_counter[right_idx]:
                matches -= 1
            elif s2_counter[right_idx] == s1_counter[right_idx]:
                matches += 1

            left_idx = ord(s2[left]) - ord('a')
            s2_counter[left_idx] -= 1
            
            
            if s2_counter[left_idx] + 1 == s1_counter[left_idx]:
                matches -= 1
            elif s2_counter[left_idx] == s1_counter[left_idx]:
                matches += 1
            left += 1
        return matches == 26

            
