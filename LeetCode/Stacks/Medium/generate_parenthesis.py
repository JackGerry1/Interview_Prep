from typing import List

def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []
    
    def backtrack(openB, closedB): 
        if openB == closedB == n: 
            res.append("".join(stack))
            return 
        
        if closedB < openB: 
            stack.append(")")
            backtrack(openB, closedB + 1)
            stack.pop()
        if openB < n: 
            stack.append("(")
            backtrack(openB + 1, closedB)
            stack.pop()
        print(stack)
    
    backtrack(0, 0)
    
    return res
    
n = 3
print(generateParenthesis(n))