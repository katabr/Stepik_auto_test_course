i = 0
j = 0
a = 0
s = 0
d = 0
b = []
m = []
while s != "end":
    s = input()
    if s != "end":

        a = s.split()
        print(a)
        l = len(a)
        print(l)
        for j in range(l):
            b.append(int(a[j]))
        print(b)
        m.append(b)
        b = []
        d += 1
        print(d)
        print(m)

l1 = l - 1
d1 = d - 1
n = []
n1 = [[0] * l for i in range(d)]
for i in range(l):
    for j in range(d):
        print(i)
        print(j)
        print(m[i][j])

        print(m[(i - 1) % l][j])
        print(m[(i + 1) % l][j])
        print(m[i][(j - 1) % d])
        print(m[i][(j + 1) % d])
        # n.append(m[(i - 1) % l][j] + m[(i + 1) % l][j] + m[i][(j - 1) % d] + m[i][(j + 1) % d])
        n1[i][j] = m[(i - 1) % l][j] + m[(i + 1) % l][j] + m[i][(j - 1) % d] + m[i][(j + 1) % d]
        j = j + 1
    i = i + 1
print(n1)
