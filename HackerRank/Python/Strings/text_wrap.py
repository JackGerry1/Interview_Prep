

def wrap(string, max_width):
    output = ""
    
    for i in range(0, len(string), max_width): 
        output += string[i:i + max_width] + "\n"
    
    return output

