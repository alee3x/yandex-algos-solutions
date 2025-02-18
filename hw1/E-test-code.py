while True:
    a = map(int, input().split())
    a = list(a)
    a = sorted(a)
    if a[0] * a[1] > a[len(a) - 1] * a[len(a) - 2]:
        print(a[0], a[1])
    else:
        print(a[-2], a[-1])
