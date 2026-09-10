class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        left = 0
        while left < len(s):
            jump = ""
            while s[left] != '#':
                jump += s[left]
                left += 1
            jump = int(jump)
            ans.append(s[left+1:left+1+jump])
            left = left+1+jump
        return ans
        



