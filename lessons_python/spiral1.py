i = 0
j = 0
k = 1
m = 0
l = 0
s = []

n = int(input())
d = n
s = [[0] * n for i in range(n)]
# print(s)

for i in range(n):
    print(*s[i])
i = 0
j = 0
s[0][0] = k
# print(s[0][0])

for m in range(d - 1):
    k = k + 1
    j = j + 1
    # print(k,i,j)
    s[i][j] = k
print(d)
while d > 0:
    d = d - 1
    for m in range(d):
        k = k + 1
        i = i + 1
        print(d)
        print(s[i][j])
        s[i][j] = k
        print(s[i][j])
    # for l in range(n):
    # print(*s[l])
    for m in range(d):
        k = k + 1
        j = j - 1
        s[i][j] = k
    # for l in range(n):
    # print(*s[l])

    d = d - 1
    for m in range(d):
        k = k + 1
        i = i - 1
        s[i][j] = k
    # for l in range(n):
    # print(*s[l])

    for m in range(d):
        k = k + 1
        j = j + 1
        s[i][j] = k

# for l in range(n):
# print(*s[l])


for l in range(n):
    print(*s[l])