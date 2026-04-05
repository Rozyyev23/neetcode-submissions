class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        open_close = { ')' : '(', ']' : '[', '}':'{'}

        for c in s:
            if c in open_close:
                if not stack or stack[-1] != open_close[c]:
                    return False
                stack.pop()
            
            else:
                stack.append(c)

        return len(stack) == 0
        