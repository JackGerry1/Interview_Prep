# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())

m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

res_set = m_set ^ n_set

res = ""

for val in sorted(res_set): 
    res += f"{val}\n"
    
print(res)
