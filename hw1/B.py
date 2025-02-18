# Майки и носки

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if (A == B) and (C == D):
    # 1 1 1 1 - 2 1 or 1 2
    if A <= C:
        print(A + 1, 1)
    else:
        print(1, C + 1)

if (A == B) and (C != D):
    # 3 3 1 4 - 4 1
    # 3 3 1 5 - 4 1
    # 3 3 1 3 - 4 1
    # 3 3 1 2 - 1 3
    # 3 3 1 6 - 4 1
    # 5 5 3 4 - 1 5
    if A < max(C, D):
        print(A + 1, 1)
    elif A == max(C, D):
        print(A + 1, 1)
    elif A > max(C, D):
        print(1, max(C, D) + 1)

if (A != B) and (C == D):
    # 1 4 3 3 - 1 4
    # 1 5 3 3 - 1 4
    # 1 3 3 3 - 1 4
    # 1 2 3 3 - 3 1
    # 1 6 3 3 - 1 4
    # 3 4 5 5 - 5 1
    if C < max(A, B):
        print(1, C + 1)
    elif C == max(A, B):
        print(1, C + 1)
    elif C > max(A, B):
        print(max(A, B) + 1, 1)

if (A != B) and (C != D):
    # 6 2 7 3 - 3 4
    # 1 2 3 4 - 3 1
    # 0 2 5 1 - 1 6
    # 0 1 0 1 - 1 1
    # 114 299 921 166 - 300 1

    # для нулей
    if A == 0:
        print(1, C + 1)
    elif B == 0:
        print(1, D + 1)
    elif C == 0:
        print(A + 1, 1)
    elif D == 0:
        print(B + 1, 1)

    # для других случаев
    elif min(A, B) + min(C, D) < min(max(A, B), max(C, D)):
        if (A - min(A, B) - 1 > 0) and (D - min(C, D) - 1 > 0):
            if max(A, B) < max(C, D):
                print(max(A, B) + 1, 1)
            else:
                print(1, max(C, D) + 1)
        elif (B - min(A, B) - 1 > 0) and (C - min(C, D) - 1) > 0:
            if max(A, B) < max(C, D):
                print(max(A, B) + 1, 1)
            else:
                print(1, max(C, D) + 1)
        else:
            print(min(A, B) + 1, min(C, D) + 1)

    else:
        if max(A, B) < max(C, D):
            print(max(A, B) + 1, 1)
        else:
            print(1, max(C, D) + 1)
