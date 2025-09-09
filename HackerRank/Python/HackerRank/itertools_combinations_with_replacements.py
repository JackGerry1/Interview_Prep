# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, length = input().split()

combos = combinations_with_replacement(sorted(string), int(length))

res = '\n'.join(f'{"".join(combo)}' for combo in combos)
print(res)
