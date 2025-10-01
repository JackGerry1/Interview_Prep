# Enter your code here. Read input from STDIN. Print output to STDOUT
english_set_length = int(input())

english_set = set(map(int, input().split()))

french_set_length = int(input()) 

french_set = set(map(int, input().split()))

intersection = english_set.intersection(french_set)

print(len(intersection))
