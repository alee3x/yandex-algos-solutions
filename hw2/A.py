# Префиксные суммы

N = int(input())
stroka = input()
output = ''
prefix_sums = [0] * (N + 1)

chisla = stroka.split()
chisla = [int(chislo) for chislo in chisla]

for i in range(1, N + 1):
    prefix_sums[i] = prefix_sums[i - 1] + chisla[i - 1]
    output = output + str(prefix_sums[i]) + ' '

output = output.strip()
print(output)
