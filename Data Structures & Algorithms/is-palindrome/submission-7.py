class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = "".join(char.lower() for char in s if char.isalnum())
        
        sizing = len(formatted)
        left, right = 0, sizing-1

        while left < right:
            if formatted[left] != formatted[right]:
                return False
            left += 1
            right -=1
        return True

