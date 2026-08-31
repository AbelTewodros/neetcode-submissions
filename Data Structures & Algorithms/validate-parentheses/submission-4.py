class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                close=stack[-1] if stack else 0
                if (i==')' and close != '(') or (i=='}' and close != '{') or (i==']' and close != '['):
                    return False
                stack.pop()
        return len(stack)==0