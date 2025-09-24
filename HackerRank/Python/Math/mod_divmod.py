# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
y = int(input())

combined_res = divmod(x, y)

print(list(combined_res)[0])
print(list(combined_res)[1])

print(combined_res)
