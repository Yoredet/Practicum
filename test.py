print('Hello World!')
n, m = map(int, input().split())
a = []
b = []
count = 0
for i in range(n):
    a.append(list(input()))
input()
for i in range(n):
    b.append(list(input()))
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1
print(count)

