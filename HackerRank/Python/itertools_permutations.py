# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations 

string, length = input().split(" ")

perms = permutations(sorted(string), int(length))

res = '\n'.join(f'{"".join(p)}' for p in perms)


print(res)