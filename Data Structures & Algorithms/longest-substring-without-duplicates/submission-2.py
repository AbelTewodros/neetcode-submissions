class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        tracker = set()
        max_len = 0

        while right < len(s):
            while s[right] in tracker:
                tracker.remove(s[left])
                left+=1
            tracker.add(s[right])
            right += 1
            max_len = max(max_len, len(tracker))
        return max_len
            