def mutate_string(string, position, character):
    # V1
    l = list(string)
    l[position] = character
    res = ''.join(l)
    return res 
    
    # V2     
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print()