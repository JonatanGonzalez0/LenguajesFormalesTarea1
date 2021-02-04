if __name__ == '__main__':
    n = int(input())
    lis = list(map(int,raw_input().strip().split()))[:n]
    x = max(lis)
    while max(lis) == x:
        lis.remove(max(lis))

    print max(lis)