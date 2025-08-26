# v1 
def merge_the_tools(string, k):
    
    substrings = []
    
    for i in range(0, len(string), k):
        substrings.append(string[i:i + k])
    
    for string in substrings: 
        unique_chars = []
        for char in string: 
            if char not in unique_chars: 
                unique_chars.append(char)
        print("".join(unique_chars))
         
        
        
# v2 
def merge_the_tools(string, k): 

    for i in range(0, len(string), k): 
        unique_chars = [] 
        
        for char in string[i:i + k]:
            if char not in unique_chars: 
                unique_chars.append(char)
        print("".join(unique_chars))

