from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens: 

        if token == "+":
            res = int(stack.pop()) + int(stack.pop())
            stack.append(res)

        elif token == "-":
            a, b = (stack.pop(), stack.pop())
            res = int(b) - int(a)
            stack.append(res)

        elif token == "*":
            res = int(stack.pop()) * int(stack.pop())
            stack.append(res)
        elif token == "/": 
            a, b = (stack.pop(), stack.pop())
            res = int(b / a)
            stack.append(res)

        else: 
            stack.append(int(token))
    
    print(f"Same as return: {stack[0]}")
    print(f"Whole Stack: {stack}")
    
    return stack[0]

def evalRPNv2(tokens: List[str]) -> int:
    stack = []
    operators = {
    "+": lambda num1, num2: num1 + num2, 
    "-": lambda num1, num2: num2 - num1, 
    "*": lambda num1, num2: num1 * num2, 
    "/": lambda num1, num2: num2 / num1
    }
    
    for token in tokens: 
        if token in operators.keys(): 
            num1 = stack.pop()
            num2 = stack.pop()
            res = operators[token](num1, num2)
            stack.append(int(res))
            
        else: 
            stack.append(int(token))
    
    print(stack[0])
    return stack[0]
    
    
tokens = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evalRPNv2(tokens)
evalRPNv2(tokens2)
evalRPNv2(tokens3)