if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s = list(set(arr))
    s.remove(max(s))
    print(max(s))
