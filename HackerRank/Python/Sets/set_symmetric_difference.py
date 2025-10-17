
set1_len = int(input())
english_set = set(map(int, input().split()))


set2_len = int(input())
french_set = set(map(int, input().split()))


sym_diff = english_set ^ french_set


print(len(sym_diff))
