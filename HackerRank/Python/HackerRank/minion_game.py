def minion_game(string):
    k_points = 0
    s_points = 0
    vowels = "AEIOU"

    for i in range(len(string)): 
        if string[i] in vowels: 
            k_points += len(string) - i
        else: 
            s_points += len(string) - i
            
    
    if s_points > k_points: 
        print(f"Stuart {s_points}")
    
    elif k_points > s_points: 
        print(f"Kevin {k_points}")
    
    else: 
        print("Draw")
    

