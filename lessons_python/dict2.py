import collections

c = collections.Counter()

i = 0
d = {}
m = set()
s = input().lower().split()
for word in (s):
    c[word] += 1
    m.add(word)
# print(word,c[word] )


l = len(m)
for word in (m):
    print(word, c[word])
0