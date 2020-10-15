a = [int(i) for i in input().split()]

n = int(input())
s = []
ss = []
i = 0
j = 0
l = len(a)
for i in range(l):

    if n == a[i]:
        ss.append(i)

if s == ss:
    print("Отсутствует")
else:

    l1 = len(ss)
    for j in range(l1):
        print(ss[j], end=" ")

