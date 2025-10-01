# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())
english_set = set(map(int, input().split()))

n_french = int(input()) 
french_set = set(map(int, input().split()))

students_in_both = english_set.union(french_set)
print(len(students_in_both))
    