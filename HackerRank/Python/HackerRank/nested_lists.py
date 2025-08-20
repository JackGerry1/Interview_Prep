if __name__ == '__main__':
    

    combined_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        combined_list.append([name, score])
    
    unique_scores = set()
    for i in range(len(combined_list)): 
        unique_scores.add(combined_list[i][1])
    sorted_scores = sorted(unique_scores)

    runner_up = sorted_scores[1]
    
    names = []
    for i in range(len(combined_list)):
        if combined_list[i][1] == runner_up: 
            names.append(combined_list[i][0])
        
    for name in sorted(names): 
        print(name)
    
