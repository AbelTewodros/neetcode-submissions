class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for i in strs:
            final_string += str(len(i)) +"#"+i
        return final_string

    def decode(self, s: str) -> List[str]:
        
        decoded_strs = []
        idx = 0
        while idx < len(s):
            jump = ""
            while s[idx] != '#':
                jump += s[idx]
                idx += 1
            jump = int(jump)
            decoded_strs.append(s[idx+1:idx+jump+1])
            idx = idx+jump+1
        return decoded_strs
