n, m = (int(i) for i in input().split())
i=0
j=0
b = [[input(int()).split() for j in range(m)] for i in range(n)]
print(b)
for j in range(m):
    for i in range(n):
        a[i,j] = input(int())




print(a)

n, m = (int(i) for i in input().split())
i=0
j=0
b = [[input() for j in range(m)] for i in range(n)]
print(b)
a = []

for j in range(m):
    for i in range(n):
        a[i,j] = input(int())
        i+=1
    j+=1




print(a)

a = 0
i = 0
b = []

while a !="end":
    if a=="end":
        a = input(str())
        b = a.split()
        i += 1
        print(b)

    else:
        break
print ("end")