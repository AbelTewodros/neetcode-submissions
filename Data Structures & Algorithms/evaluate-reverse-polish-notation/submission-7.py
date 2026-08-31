class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        keep_track=[]
        for i in tokens:
            if i=='+':
                keep_track.append(keep_track.pop()+keep_track.pop())
            elif i=='-':
                a,b=keep_track.pop(),keep_track.pop()
                keep_track.append(b-a)
            elif i=='*':
                keep_track.append(keep_track.pop()*keep_track.pop())
            elif i=='/':
                a,b=keep_track.pop(),keep_track.pop()
                keep_track.append(int(float(b)/a))
            else:
                keep_track.append(int(i))
        return keep_track[0]

