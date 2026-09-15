class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(openN, closeN):
            if openN == closeN == n: ## reached the limit
                res.append("".join(stack))
                return
            
            if openN < n: ## can add more opening parentheses
                stack.append("(")
                back(openN+1, closeN)
                stack.pop()
            

            if closeN < openN: ## closed should always be less than open
                stack.append(")")
                back(openN, closeN + 1)
                stack.pop()
        
        back(0,0)
        return res