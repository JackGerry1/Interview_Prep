# Enter your code here. Read input from STDIN. Print output to STDOUT

set_a = set(map(int, input().split()))

num_other_sets = int(input())

is_strict_superset = True


for _ in range(num_other_sets): 
    other_set = set(map(int, input().split()))
    
    if not set_a.issuperset(other_set):
        is_strict_superset = False

print(is_strict_superset)
