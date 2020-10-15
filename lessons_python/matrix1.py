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
print(m)
print(d)
n = []
for i in range(l):
    for j in range(d):
        n[i][j] = m[(i - 1) % l][j] + m[(i + 1) % l][j] + m[i][(j - 1) % d] + m[i][(j + 1) % d]
print(n)
