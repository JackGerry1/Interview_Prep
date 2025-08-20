if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_arr = list(arr)
    
    max_value = max(list_arr)
    
    while max_value in list_arr:
        list_arr.remove(max_value)    

    runner_up = max(list_arr)
    print(runner_up)    
        