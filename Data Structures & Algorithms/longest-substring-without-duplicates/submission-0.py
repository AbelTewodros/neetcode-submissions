class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       longest=0
       track=set()
       l=0
       for i in range(len(s)):
            while s[i] in track:
                track.remove(s[l])
                l+=1
            track.add(s[i])
            longest=max(longest,i-l+1)
       return longest

       
    
                
