if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_scores = set(arr)
    unique_scores.discard(max(unique_scores))
    print(max(unique_scores))