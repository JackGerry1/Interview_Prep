# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())

res = pow(a, b)
mod_res = pow(a, b, m)
print(res)
print(mod_res)
