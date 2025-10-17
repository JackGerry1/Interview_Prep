from collections import Counter

K = int(input())
rooms = list(map(int, input().split()))

# Count occurrences
counts = Counter(rooms)

# Find the one with count == 1
for room, freq in counts.items():
    if freq == 1:
        print(room)
        break
