# Плот

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x > x2:
    if y1 < y < y2:
        print("E")
    elif y > y2:
        print("NE")
    elif y < y1:
        print("SE")
elif x < x1:
    if y1 < y < y2:
        print("W")
    elif y > y2:
        print("NW")
    elif y < y1:
        print("SW")
elif x1 < x < x2:
    if y > y2:
        print("N")
    elif y < y1:
        print("S")
