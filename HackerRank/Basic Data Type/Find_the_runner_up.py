from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(Counter(map(int, input().split())).keys()))
    print(arr[-2])
