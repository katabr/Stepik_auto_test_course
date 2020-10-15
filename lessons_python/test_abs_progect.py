



import collections




c = collections.Counter()


m = set()
s = input().lower().split()
for word in (s):
    c[word] += 1
    m.add(word)

for word in (m):
    print(word,c[word] )