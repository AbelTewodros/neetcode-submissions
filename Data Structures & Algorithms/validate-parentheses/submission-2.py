class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                close=stack.pop()
                if (i==')' and close != '(') or (i=='}' and close != '{') or (i==']' and close != '['):
                    return False
        return len(stack)==0