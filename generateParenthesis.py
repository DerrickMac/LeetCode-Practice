def generateParenthesis(n):
    
    stack = []
    res = []

    def backtrack(openN, closedN):
        
        # valid IIF open == closed == n
        if openN == closedN == n:
            res.append("".join(stack))
            return

        # only add open parenthesis if open < n    
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        # only add a closing parenthesis if closed < open    
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0,0)
    return res

# test input
print(generateParenthesis(3))