n = int(input())

for i in range(1, n // 2 + 1):
    s = n - 2 * i
    if s > 0:
        print("*" * i + " " * s + "*" * i)

print("*" * n)


for i in range(n // 2, 0, -1):
    s = n - 2 * i
    if s > 0:
        print("*" * i + " " * s + "*" * i)