
# this code is better but had to google it to get it, but i understood the concept. 
def isValid(s: str) -> bool:
    close_to_open = {")": "(", "]": "[", "}": "{"}
    stack = []
    
    for char in s: 
        if char in close_to_open.keys(): 
            if stack and stack[-1] == close_to_open[char]:
                print(close_to_open[char])
                stack.pop()
            else: 
                return False
        else: 
            stack.append(char)
    return True if not stack else False

# this ran quicker but had the same time complexity but the code is worse. 
def isValidv2(s: str) -> bool:
    stack = []
    
    for char in s: 
        if stack and char == ")" and stack[-1] == "(": 
            stack.pop()
        elif stack and char == "]" and stack[-1] == "[": 
            stack.pop()
        elif stack and char == "}" and stack[-1] == "{": 
            stack.pop()
        else: 
            stack.append(char)
    return True if not stack else False



