class Solution:
    def isValid(self, s: str) -> bool:
        def match(i, j):
            if (i=='(' and j==')') or (i=='[' and j==']') or (i=='{' and j=='}'):
                return True
            return False
        
        stack = [-1]
        chars = "{}[]()"
        for i in s:
            if i in chars:
                if match(stack[-1], i):
                    stack.pop()
                else:
                    stack.append(i)
        if stack[0] == -1 and len(stack) == 1:
            return True
        return False
                