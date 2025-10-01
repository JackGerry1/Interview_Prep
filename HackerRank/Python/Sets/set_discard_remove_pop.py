n = int(input())
s = set(map(int, input().split()))
command_number = int(input())

for i in range(command_number): 
    command = input().split()
    if command[0] == "remove" and int(command[1]) in s:
        s.remove(int(command[1])) 
    if command[0] == "discard":
        s.discard(int(command[1]))  
    if command[0] == "pop":
        s.pop()

print(sum(s))

