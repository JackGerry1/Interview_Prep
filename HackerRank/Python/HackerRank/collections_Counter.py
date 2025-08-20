# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = number of shoes, N = number of customers, xi = price of shoe and shoe size for next N lines. 

X = int(input())
shoes_list = list(map(int, list(input().split())))
N = int(input())

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
