# Город Че

input_1 = input()
input_2 = input()

n, r = map(int, input_1.split())
distances = input_2.split()
distances = [int(num) for num in distances]

# boys will see each other if the distance between them is <= r
R = 1
counter = 0
for L in range(0, n):
    while (distances[R] - distances[L] <= r) and (R < n - 1):
        R += 1
    if distances[R] - distances[L] > r:
        counter += (len(distances) - R)

print(counter)
