import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()
                match i:
                    case '+':
                        a += b
                    case '-':
                        a -= b
                    case '*':
                        a *= b
                    case '/':
                        a = int(a/b)
                stack.append(a)
            else:
                stack.append(int(i))
        return stack.pop()