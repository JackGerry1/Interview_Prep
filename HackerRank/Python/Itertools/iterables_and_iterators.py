# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

N = input()
str_array = input().split()
K = input()

all_combos = list(itertools.combinations(str_array, int(K)))

count = 0
for combo in all_combos: 
    if "a" in combo: 
        count += 1

res = count / len(all_combos)

print(res)
