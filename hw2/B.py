# Сумма номеров

input_1 = input()
input_2 = input()

N, K = map(int, input_1.split())
nomera = input_2.split()
nomera = [int(num) for num in nomera]

prefix_sums = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sums[i] = prefix_sums[i - 1] + nomera[i - 1]

R = 1
counter = 0
for L in range(1, N + 1):
    while (prefix_sums[R] - prefix_sums[L - 1] < K) and (R < N):
        R += 1
    if prefix_sums[R] - prefix_sums[L - 1] == K:
        counter += 1

print(counter)
