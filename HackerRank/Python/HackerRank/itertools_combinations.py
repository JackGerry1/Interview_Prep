# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string, length = input().split()
length = int(length)

string = sorted(string)

for i in range(1, length + 1):
    combos = combinations(string, i)
    for combo in combos:
        print(f'{"".join(combo)}')
