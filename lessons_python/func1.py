n = int(input())
x = []
y = []
i = 0

for i in range(n):
    x.append(int(input()))
    y.append(f(x[i]))
    i = i + 1

i = 0
for i in range(n):
    print(y[i])





