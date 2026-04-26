class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False 

                x = stack.pop()

                if x == '(' and c != ')':
                    return False
                if x == '[' and c != ']':
                    return False
                if x == '{' and c != '}':
                    return False

        return len(stack) == 0 
