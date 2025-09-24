if __name__ == '__main__':
    N = int(input())
    res = []
    
    for i in range(N):
        line = input().split()
        command = line[0]
        if command == "insert":
            index = int(line[1])
            value = int(line[2])
            
            res.insert(index, value)
            
        elif command == "print":
            print(res)
            
        elif command == "remove":
            value = int(line[1])
            res.remove(value)
            
        elif command == "append":
            value = int(line[1])
            res.append(value)
            
        elif command == "sort":
            res.sort()
            
        elif command == "pop":
            res.pop()
            
        elif command == "reverse":
            res.reverse()
