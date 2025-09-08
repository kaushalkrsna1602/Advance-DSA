from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: int(b / a)  # truncates toward zero
        }
        
        for token in tokens:
            if token in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        
        return stack.pop()