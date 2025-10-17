# Enter your code here. Read input from STDIN. Print output to STDOUT

arr_len, set_len = map(int, input().split())
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
happiness = 0

for i in range(len(arr)): 
    if arr[i] in set_A: 
        happiness += 1
    if arr[i] in set_B: 
        happiness -= 1

print(happiness)


