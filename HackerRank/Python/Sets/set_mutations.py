_ = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd, _ = input().split() 
    s2 = set(map(int, input().split()))
    
    
    getattr(s1, cmd)(s2)

print(sum(s1))
