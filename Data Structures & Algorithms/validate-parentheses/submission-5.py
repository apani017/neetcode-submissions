class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if pop != pairs[c]:
                        return False
        return not stack
            