# Enter your code here. Read input from STDIN. Print output to STDOUT
english_num = int(input())

english_set = set(map(int, input().split()))

french_num = int(input())
french_set = set(map(int, input().split()))

english_only = english_set.difference(french_set)

print(len(english_only)) 
