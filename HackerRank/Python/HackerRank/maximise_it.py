
# SOLUTION 1
from itertools import product
K, M = map(int, input().split())


nums = []
sums = []
for _ in range(K): 
    nums.append(list((map(int, input().split()[1:]))))

for i in range(len(nums)):
    for j in range(len(nums[i])):
        nums[i][j] = nums[i][j] ** 2

product_combos = product(*nums)

for combo in product_combos: 
    sums.append(sum(combo) % M)

print(max(sums))

# SOLUTION 2 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())


nums = []
sums = []
for _ in range(K): 
    row = map(int, input().split()[1:])
    nums.append(map(lambda x: x ** 2, row))
    
for combo in product(*nums): 
    sums.append(sum(combo) % M)

print(max(sums))
    

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())

nums = []

for _ in range(K): 
    row = (map(int, input().split()[1:]))
    nums.append(map(lambda x:x**2, row)) 
    
print(max(map(lambda x: sum(x) % M, product(*nums))))

