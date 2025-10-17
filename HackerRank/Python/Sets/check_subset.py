T = int(input())

for _ in range(T):     
    
    a_len = int(input())
    A = set(map(int, input().split()))
    
    # Read Set B
    b_len = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
