# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = number of shoes, N = number of customers, xi = price of shoe and shoe size for next N lines. 

from collections import Counter

X = int(input()) 
shoes_list = Counter(map(int, input().split()))

N = int(input())

revenue = 0 

for _ in range(N): 
    size, price = map(int, input().split())
    
    if shoes_list[size] > 0: 
        revenue += price
        shoes_list[size] -= 1
        
print(revenue)