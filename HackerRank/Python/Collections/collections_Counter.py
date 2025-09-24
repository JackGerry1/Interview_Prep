# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = number of shoes, N = number of customers, xi = price of shoe and shoe size for next N lines. 

X = int(input())
shoes_list = list(map(int, list(input().split())))

N = int(input())

print(shoes_list)

shoe_pairs = []
for _ in range(N): 
    shoe_size, price = map(int, input().split())
    shoe_pairs.append((shoe_size, price))


revenue = 0
for i in range(len(shoe_pairs)): 
    if shoe_pairs[i][0] in shoes_list: 
        revenue += shoe_pairs[i][1]
        shoes_list.remove(shoe_pairs[i][0])

print(revenue)

# better version using collections.Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = number of shoes, N = number of customers, xi = price of shoe and shoe size for next N lines. 

from collections import Counter

shoe_number = int(input())
shoe_list = Counter(map(int, input().split()))
customer_number = int(input())

income = 0

for i in range(customer_number): 
    size, price = map(int, input().split())
    if shoe_list[size]:
        income += price 
        shoe_list[size] -= 1 

print(income)
    

