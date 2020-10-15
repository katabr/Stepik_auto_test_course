i = 0
j = 0
k = 1
m = 0
l = 0
s = []

n = int(input())
d = n
s = [[0] * n for i in range(n)]
print(s)

for i in range(n):
    print(*s[i])

s[0][0] = k
for m in range(d):
    k = k + 1
    j = j + 1
    s[i][j] = k

while d > 0:
    d = d - 1
    for m in range(d):
        k = k + 1
        i = i + 1
        s[i][j] = k
    for m in range(d):
        k = k + 1
        j = j - 1
        s[i][j] = k
    d = d - 1
    for m in range(d):
        k = k + 1
        i = i - 1
        s[i][j] = k
    for m in range(d):
        k = k + 1
        j = j + 1
        s[i][j] = k





for l in range(n):
    print(*s[i])
