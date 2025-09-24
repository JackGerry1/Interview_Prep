

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    res = ""
    for word in words:
        res += word.capitalize() + " "
        
    return res

