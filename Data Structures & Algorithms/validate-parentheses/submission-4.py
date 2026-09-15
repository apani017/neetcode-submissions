class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = { ")" : "(", "]" : "[", "}" : "{" }
        
        # [()]
        for c in s:
            if c not in mapped: # c is an opening bracket
                stack.append(c)
            else: # c is a closing bracket
                if not stack:
                    return False # c is closing but stack empty
                else:
                    popped = stack.pop()
                    if popped != mapped[c]:
                        return False
        return not stack