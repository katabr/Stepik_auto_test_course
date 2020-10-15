n = int(input())
x = []
y = []
i = 0
d = {}
for i in range(n):
    x.append(int(input()))
    if x[i] in d.keys():
        y.append(d[x[i]])
        i = i + 1
    else:
        y.append(f(x[i]))
        d[x[i]] = y[i]
        i = i + 1
for val in a.values():
    print(val)

i = 0
for i in range(n):
    print(y[i])
