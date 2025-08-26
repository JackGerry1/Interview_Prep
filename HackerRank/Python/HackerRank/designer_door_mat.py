# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

# Top part
for i in range(1, N, 2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)

# Middle line
print("WELCOME".center(M, "-"))

# Bottom part (mirror of top)
for i in range(N-2, 0, -2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)


